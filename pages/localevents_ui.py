import streamlit as st
import pandas as pd
import numpy as np
import joblib
import requests
from math import radians, sin, cos, sqrt, atan2

# ------------------------------------------------------------
# Load data once
@st.cache_data
def load_data():
    walmart_df = pd.read_csv('walmart_info.csv')
    events_df = pd.read_csv('city_venue_concert.csv')
    for df in [walmart_df, events_df]:
        df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    return walmart_df, events_df

walmart_df, events_df = load_data()

# ------------------------------------------------------------
# Load trained model once
@st.cache_resource
def load_model():
    return joblib.load('sales_model.pkl')

model = load_model()

# ------------------------------------------------------------
# Helper: Geocode venue name → (latitude, longitude) using Nominatim (no key needed)
def get_lat_lon_from_address(address):
    st.info(f"Geocoding address: {address}")
    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": address, "format": "json"}
    headers = {"User-Agent": "WalmartSalesPredictor/1.0 (contact@example.com)"}
    response = requests.get(url, params=params, headers=headers)
    if response.status_code != 200 or not response.json():
        raise Exception("Failed to geocode address. Try a more specific venue.")
    data = response.json()
    lat = float(data[0]['lat'])
    lon = float(data[0]['lon'])
    return lat, lon

# ------------------------------------------------------------
# Helper: Haversine distance
def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    phi1, phi2 = radians(lat1), radians(lat2)
    dphi = radians(lat2 - lat1)
    dlambda = radians(lon2 - lon1)
    a = sin(dphi/2)**2 + cos(phi1)*cos(phi2)*sin(dlambda/2)**2
    return R * 2 * atan2(sqrt(a), sqrt(1 - a))

# ------------------------------------------------------------
# Streamlit UI
st.title("🏬 Walmart Event Sales Predictor")

st.markdown("""
Enter your event details to predict sales uplift for the nearest Walmart store.
""")

venue_name = st.text_input("📍 Venue Name (e.g. Pragati Maidan, Delhi)", "")
attendees = st.number_input("👥 Expected Attendees", min_value=1, value=1000)
event_name_input = st.text_input("🎵 Event Name (as in your dataset)", "")

if st.button("Predict Sales"):
    try:
        if not venue_name or not event_name_input:
            st.error("Please enter both Venue Name and Event Name.")
        else:
            # 1️⃣ Geocode venue name
            latitude, longitude = get_lat_lon_from_address(venue_name)
            st.success(f"Geocoded to: {latitude:.5f}, {longitude:.5f}")

            # 2️⃣ Find nearest Walmart
            walmart_df['distance_km'] = walmart_df.apply(
                lambda row: haversine(latitude, longitude, row['latitude'], row['longitude']),
                axis=1
            )
            nearest_store = walmart_df.loc[walmart_df['distance_km'].idxmin()]
            store_address = nearest_store['store_name']
            store_population = nearest_store['population_within_5km']

            # 3️⃣ Add attendees to population
            total_population = store_population + attendees

            # 4️⃣ Find event impact
            event_match = events_df[events_df['event_name'].str.lower() == event_name_input.lower()]
            if event_match.empty:
                st.error(f"Event '{event_name_input}' not found in dataset.")
            else:
                event_impact_score = event_match.iloc[0]['event_impact_score']

                # 5️⃣ Predict sales
                X_input = pd.DataFrame([{
                    'population': total_population,
                    'event_name': event_name_input,
                    'event_impact_score': event_impact_score
                }])
                predicted_sales = model.predict(X_input)[0]

                # 6️⃣ Display
                st.subheader("✅ Prediction Result")
                st.markdown(f"**Nearest Walmart Store:** {store_address}")
                st.markdown(f"**Predicted Sales:** ₹ {round(predicted_sales, 2):,.2f}")
    except Exception as e:
        st.error(f"❌ Error: {e}")
