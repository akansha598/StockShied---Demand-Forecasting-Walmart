

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import requests
import os
from math import radians, sin, cos, sqrt, atan2
import altair as alt
import plotly.express as px
import json
import time
import pydeck as pdk

# ------------------------------------------------------------
st.set_page_config(page_title="Walmart Event Sales Predictor", layout="wide")

# ------------------------------------------------------------
# Load data once
@st.cache_data
def load_data():
    THIS_DIR = os.path.dirname(__file__)
    walmart_csv = os.path.join(THIS_DIR, "walmart_info.csv")
    events_csv = os.path.join(THIS_DIR, "city_venue_concert.csv")
    
    walmart_df = pd.read_csv(walmart_csv)
    events_df = pd.read_csv(events_csv)

    for df in [walmart_df, events_df]:
        df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
        for col in df.select_dtypes(include='object').columns:
            df[col] = df[col].str.strip()
            
    events_df['event_impact_score'] = pd.to_numeric(events_df['event_impact_score'], errors='coerce')

    return walmart_df, events_df

walmart_df, events_df = load_data()


# ------------------------------------------------------------
# Load trained model once
# @st.cache_resource
# def load_model():
#     REPO_ROOT = os.path.dirname(os.path.dirname(file))
#     model_path = os.path.join(REPO_ROOT, 'sales_model.pkl')
#     return joblib.load(model_path)


# model = load_model()

@st.cache_resource
def load_model():
    model_bundle = joblib.load("sales2_model.pkl")
    return model_bundle

model_bundle = load_model()


model = load_model()
# ------------------------------------------------------------
def get_lat_lon_from_address(address, max_retries=3):
    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": address, "format": "json"}
    headers = {"User-Agent": "WalmartSalesPredictor/1.0 (contact@example.com)"}

    for attempt in range(max_retries):
        try:
            response = requests.get(url, params=params, headers=headers, timeout=10)
            response.raise_for_status()
            data = response.json()
            if not data:
                raise ValueError("No results returned from geocoder.")
            lat = float(data[0]['lat'])
            lon = float(data[0]['lon'])
            return lat, lon
        except Exception as e:
            print(f"Attempt {attempt+1} failed: {e}")
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
            else:
                raise Exception(f"Geocoding failed after {max_retries} attempts: {e}")

# ------------------------------------------------------------
# Helper: Haversine distance
def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    phi1, phi2 = radians(lat1), radians(lat2)
    dphi = radians(lat2 - lat1)
    dlambda = radians(lon2 - lon1)
    a = sin(dphi/2)**2 + cos(phi1)*cos(phi2)*sin(dlambda/2)**2
    return R * 2 * atan2(sqrt(a), sqrt(1 - a))

def show_alerts_in_sidebar_area(col):
    if not hasattr(col, "markdown"):
        st.error("show_alerts_in_sidebar_area: invalid Streamlit container passed!")
        return
    col.subheader("📋 Overstock Alerts")

    if os.path.exists("alerts.csv"):
        alert_data = pd.read_csv("alerts.csv")

        if alert_data.empty:
            col.info("No alerts added yet.")
        else:
            # Clean headers
            alert_data.columns = alert_data.columns.str.strip()

            # Clean data cells
            for column in alert_data.select_dtypes(include='object').columns:
                alert_data[column] = alert_data[column].str.strip()

            for _, row in alert_data.iterrows():
                store_name = row.get('Store Name', 'N/A')
                store_location = row.get('Store Location', 'N/A')
                overstock_data = row.get('Overstock Data', 'N/A')

                alert_html = f"""
                    <div style="
                        background-color: #fff8f0;
                        border: 3px solid #ff6f61;
                        border-radius: 12px;
                        padding: 16px;
                        margin-bottom: 16px;
                        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
                        font-family: Arial, sans-serif;
                    ">
                        <h4 style="margin-top:0; color:#d84315;">🏪 {store_name}</h4>
                        <p style="margin:4px 0; color:#150;"><b>📍 Location:</b> {store_location}</p>
                        <p style="margin:4px 0; color:black;"><b>📦 Overstock Data:</b> {overstock_data}</p>
                    </div>
                """
                col.markdown(alert_html, unsafe_allow_html=True)
    else:
        col.info("No alerts added yet.")


def find_closest_overstock_store(pred_lat, pred_lon):
    if not os.path.exists("alerts.csv"):
        return None

    alert_data = pd.read_csv("alerts.csv")

    if alert_data.empty:
        return None

    # Clean columns and data
    alert_data.columns = alert_data.columns.str.strip()
    for col in alert_data.select_dtypes(include='object').columns:
        alert_data[col] = alert_data[col].str.strip()


    # Add lat/lon for each alert store location using exact address from CSV
    for idx, row in alert_data.iterrows():
        raw_location = str(row['Store Location']).strip()

        try:
            time.sleep(1)  # polite delay for Nominatim
            lat, lon = get_lat_lon_from_address(raw_location)
            print(f"📍 '{raw_location}' → ({lat}, {lon})")

            alert_data.at[idx, 'lat'] = lat
            alert_data.at[idx, 'lon'] = lon
        except Exception as e:
            print(f"❌ Geocoding failed for {raw_location}: {e}")
            alert_data.at[idx, 'lat'] = None
            alert_data.at[idx, 'lon'] = None

    # Drop any rows without valid lat/lon
    alert_data['lat'] = pd.to_numeric(alert_data['lat'], errors='coerce')
    alert_data['lon'] = pd.to_numeric(alert_data['lon'], errors='coerce')
    alert_data = alert_data.dropna(subset=['lat', 'lon'], how='any')

    if alert_data.empty:
        return None

    # Calculate distance to prediction point
    alert_data['distance_km'] = alert_data.apply(
        lambda r: haversine(pred_lat, pred_lon, r['lat'], r['lon']),
        axis=1
    )

    # Find closest store under 50 km
    closest = alert_data.loc[alert_data['distance_km'].idxmin()]
    if closest['distance_km'] > 50:
        return None

    return closest


def remove_alert_row(store_name, store_location, overstock_data):
    if not os.path.exists("alerts.csv"):
        return

    alert_data = pd.read_csv("alerts.csv")
    alert_data.columns = alert_data.columns.str.strip()

    # Remove matching row
    alert_data = alert_data[
        ~(
            (alert_data['Store Name'] == store_name) &
            (alert_data['Store Location'] == store_location) &
            (alert_data['Overstock Data'] == overstock_data)
        )
    ]

    alert_data.to_csv("alerts.csv", index=False)

# ------------------------------------------------------------
# Sidebar Feature Selector
st.sidebar.title("🗂 Select Feature")
selected_feature = st.sidebar.radio(
    "Choose a feature to use:",
    ["Sales Prediction", "Overstock Alerts"]
)

# ------------------------------------------------------------
# Split entire page horizontally: 70% (main area), 30% (alerts)
main_col, alert_col = st.columns([0.7, 0.3], gap="large")

# ------------------------------------------------------------
# Always show alerts on the right
show_alerts_in_sidebar_area(alert_col)

# ------------------------------------------------------------
# Main area content changes based on selection
with main_col:

    # 1️⃣ Sales Prediction Page
    if selected_feature == "Sales Prediction":
        st.title("🏬 Walmart Event Sales Predictor")

        # Initialize session state
        if "prediction_done" not in st.session_state:
            st.session_state.prediction_done = False
        if "results" not in st.session_state:
            st.session_state.results = {}

        # ------------------------------------------------------------
        # Form UI and Logic
        if not st.session_state.prediction_done:
            with st.form(key='prediction_form'):
                st.markdown("Enter your event details to predict sales uplift for the nearest Walmart store.")

                venue_name = st.text_input("📍 Venue Name (e.g. Pragati Maidan, Delhi)", "")
                attendees = st.number_input("👥 Expected Attendees", min_value=1, value=1000)
                event_name_input = st.text_input("🎵 Event Name (as in your dataset)", "")

                submit_button = st.form_submit_button("Predict Sales")

                if submit_button:
                    try:
                        if not venue_name or not event_name_input:
                            st.error("Please enter both Venue Name and Event Name.")
                        else:
                            # Step 1: Geocode
                            latitude, longitude = get_lat_lon_from_address(venue_name)

                            # Step 2: Nearest Walmart
                            walmart_df['distance_km'] = walmart_df.apply(
                                lambda row: haversine(latitude, longitude, row['latitude'], row['longitude']),
                                axis=1
                            )
                            nearest_store = walmart_df.loc[walmart_df['distance_km'].idxmin()]
                            store_name = nearest_store['store_name']
                            store_address = nearest_store['address']
                            store_city= nearest_store['city']
                            store_state= nearest_store['state']
                            store_population = nearest_store['population_within_5km']
                            
                            avg_monthly_sales_inr = nearest_store.get('avg_monthly_sales_inr', None)

                            if avg_monthly_sales_inr is None:
                                raise Exception("Missing 'avg_monthly_sales_INR' column in Walmart dataset.")

                            # Step 3: Add attendees
                            total_population = store_population + attendees

                            # Step 4: Match event
                            event_match = events_df[events_df['event_name'].str.lower() == event_name_input.lower()]
                            if event_match.empty:
                                st.error(f"Event '{event_name_input}' not found in dataset.")
                            else:
                                event_impact_score = event_match.iloc[0]['event_impact_score']

                                # Step 5: Predict
                               # Step 5: Predict
#                                 X_input = pd.DataFrame({
#                                     'population': pd.Series([total_population], dtype=float),
#                                     'event_name': pd.Series([event_name_input], dtype=str),
#                                     'event_impact_score': pd.Series([event_impact_score], dtype=float)
#                                 })



# # Ensure column order matches training data
                                

#                                 predicted_sales = model.predict(X_input)[0]
                                # Encode event name
                                event_label = model_bundle['label_encoder'].transform([event_name_input.strip()])[0]

                                # Make sure your input matches the training columns
                                X_input = np.array([[float(total_population), float(event_label), float(event_impact_score)]])

                                # Scale
                                X_scaled = model_bundle['scaler'].transform(X_input)

                                # Predict
                                predicted_sales = model_bundle['regressor'].predict(X_scaled)[0]




                                # Step 6: Compare with past sales
                                pct_change = ((predicted_sales - avg_monthly_sales_inr) / avg_monthly_sales_inr) * 100
                                recommendation = "Increase" if pct_change > 0 else "Decrease"
                                pct_change_display = abs(round(pct_change, 2))
                                # Step 7: Store results and rerun
                                st.session_state.results = {
                                    "store_name": store_name,
                                    "address" : store_address,
                                    "city" : store_city,
                                    "state" : store_state,
                                    "latitude": latitude,
                                    "longitude": longitude,
                                    "predicted_sales": predicted_sales,
                                    "avg_monthly_sales_inr": avg_monthly_sales_inr,
                                    "pct_change": pct_change,
                                    "recommendation": recommendation,
                                    "pct_change_display": pct_change_display
                                }
                                st.session_state.prediction_done = True
                                st.rerun()

                    except Exception as e:
                        st.error(f"❌ Error: {e}")

        # ------------------------------------------------------------
        # Display prediction results
        if st.session_state.prediction_done:
            results = st.session_state.results

            st.subheader("✅ Prediction Result")
            st.markdown(f"Nearest Walmart Store: {results['store_name']}")
            st.markdown(f"Nearest Walmart Store Location: {results['address']},{results['city']},{results['state']}")
            st.markdown(f"Predicted Sales: ₹ {round(results['predicted_sales'], 2):,.2f}")
            st.markdown(f"Average Monthly Sales: ₹ {round(results['avg_monthly_sales_inr'], 2):,.2f}")

            if results['recommendation'] == "Increase":
                st.success(f"📈 Predicted increase of approximately {results['pct_change_display']}% over average sales.")
                st.success(f"🛒 Recommendation: Increase stock upto {results['pct_change_display']}%")
            else:
                st.warning(f"📉 Predicted decrease of approximately {results['pct_change_display']}% from average sales.")
                st.warning(f"🛒 Recommendation: Decrease stock upto {results['pct_change_display']}%")


            st.divider()
            st.subheader("📦 Check Nearby Overstock Stores")

            with st.spinner("Checking nearby overstock stores..."):
                closest_alert = find_closest_overstock_store(results['latitude'], results['longitude'])

            if closest_alert is None:
                st.info("✅ No nearby overstock stores found in alerts.")
            else:
                st.markdown(
                    f"""
                    ### Closest Overstock Store  
                    🏪 {closest_alert['Store Name']}  <br>
                    📍 Location: {closest_alert['Store Location']}  <br>
                    📦 Overstock Data: {closest_alert['Overstock Data']}  <br>
                    📏 Approx. Distance: {round(closest_alert['distance_km'], 2)} km
                    """,
                    unsafe_allow_html=True
                )

    
                if st.button("✅ Take Stock from this Store"):
                    remove_alert_row(
                        closest_alert['Store Name'],
                        closest_alert['Store Location'],
                        closest_alert['Overstock Data']
                    )
                    st.success("✅ Overstock alert removed! Stock transfer logged.")
                    st.rerun()
                else:
                    st.info("❌ No action taken.")
                    
            
                    
            
            st.subheader("🗺 Store Locations on Map")
            # Define map points with colors
            map_points = pd.DataFrame({
                "Store": [
                    "Predicted Walmart Store",
                    "Overstock Alert Store"
                ],
                "StoreLocation": [
                    results['address'],
                    closest_alert['Store Location']
                ],
                "lat": [
                    results['latitude'],
                    closest_alert['lat']
                ],
                "lon": [
                    results['longitude'],
                    closest_alert['lon']
                ],
                "color": [
                    [0, 128, 255],    # Blue for Walmart prediction
                    [255, 100, 100]   # Red for Overstock Alert
                ]
            })

                # Define PyDeck layer
            layer = pdk.Layer(
                'ScatterplotLayer',
                data=map_points,
                get_position='[lon, lat]',
                get_fill_color='color',
                get_radius=3000,
                pickable=True,
            )

# Define view state and tooltip
            view_state = pdk.ViewState(
                latitude=map_points["lat"].mean(),
                longitude=map_points["lon"].mean(),
                zoom=8,
                pitch=0
            )

            tooltip = {
                "html": "<b>{Store}</b><br/>{StoreLocation}<br/>Lat: {lat}<br/>Lon: {lon}",
                "style": {"backgroundColor": "steelblue", "color": "white"}
            }
            st.markdown("""
                <div style="display: flex; gap: 20px; margin-bottom: 1rem;">
                    <div style="display: flex; align-items: center;">
                        <div style="width: 14px; height: 14px; background-color: #0078FF; border-radius: 50%; margin-right: 8px;"></div>
                        <span>Predicted Walmart Store</span>
                    </div>
                    <div style="display: flex; align-items: center;">
                        <div style="width: 14px; height: 14px; background-color: #FF6464; border-radius: 50%; margin-right: 8px;"></div>
                        <span>Overstock Alert Store</span>
                    </div>
                </div>
            """, unsafe_allow_html=True)

# Render the map
            st.pydeck_chart(pdk.Deck(
                layers=[layer],
                initial_view_state=view_state,
                tooltip=tooltip
            ))
            
            st.subheader("🟢 Sales Distribution")
            pie_chart_data = pd.DataFrame({
                'Category': ['Average Monthly Sales', 'Predicted Sales'],
                'Amount': [results['avg_monthly_sales_inr'], results['predicted_sales']]
            })
            st.plotly_chart(
                px.pie(
                    pie_chart_data,
                    names='Category',
                    values='Amount',
                    title='Sales Share'
                ),
                use_container_width=True
            )

            st.button("🔄 Reset", on_click=lambda: st.session_state.update({
                    "prediction_done": False,
                    "results": {}
            }))

    # 2️⃣ Overstock Alerts Page
    elif selected_feature == "Overstock Alerts":
        st.title("📦 Add New Overstock Alert")
        with st.form(key="alert_form"):
            alert_store_name = st.text_input("🏪 Store Name")
            alert_store_location = st.text_input("📍 Store Location")
            alert_data = st.text_area("📦 Overstock Data")
            alert_submit = st.form_submit_button("Add Alert")

            if alert_submit:
                if alert_store_name and alert_store_location and alert_data:
                    new_alert = pd.DataFrame([{
                        "Store Name": alert_store_name,
                        "Store Location": alert_store_location,
                        "Overstock Data": alert_data
                    }])
                    try:
                        if os.path.exists("alerts.csv"):
                            existing_alerts = pd.read_csv("alerts.csv")
                            updated_alerts = pd.concat([existing_alerts, new_alert], ignore_index=True)
                        else:
                            updated_alerts = new_alert

                        updated_alerts.to_csv("alerts.csv", index=False)
                        st.success("✅ Alert added successfully!")
                        st.rerun()
                    except Exception as e:
                        st.error(f"❌ Failed to save alert: {e}")
                else:

                    st.warning("⚠ Please fill in all fields.")
