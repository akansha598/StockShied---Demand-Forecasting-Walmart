import streamlit as st
import pandas as pd
import numpy as np
import requests
import joblib
from datetime import datetime


st.set_page_config(page_title="Festival Demand Surge")




# Load the trained festival model
model = joblib.load("festival_model.pkl")

# Default values for non-festival features
default_features = {
    "Fuel_Price": 3.2,
    "CPI": 211.3,
    "Unemployment": 7.2,
    "Temperature": 22.0
}

# Fetch upcoming holidays using Calendarific
@st.cache_data
def fetch_festivals(country, year):
    API_KEY = ""
    url = f"https://calendarific.com/api/v2/holidays?&api_key={API_KEY}&country={country}&year={year}"
    res = requests.get(url)
    data = res.json()
    holidays = [
        {
            "name": item["name"],
            "date": item["date"]["iso"]
        }
        for item in data["response"]["holidays"]
        if item["type"] and "National holiday" in item["type"]
    ]
    df = pd.DataFrame(holidays)
    df["date"] = pd.to_datetime(df["date"])
    upcoming = df[df["date"] >= pd.Timestamp.today()].sort_values("date")
    return upcoming.head(7)

# Streamlit UI
st.title("🎉 Festival-Based Walmart Sales Forecast")
st.markdown("Predict sales based on upcoming festivals in any country.")

country = st.selectbox("🌍 Select Country Code:", ["US", "IN", "CA", "MX", "BR", "AR", "ZA"])
year = datetime.today().year

festivals_df = fetch_festivals(country, year)

if not festivals_df.empty:
    st.success("✅ Fetched upcoming festivals")

    st.subheader("🎛️ What-If Festival Simulation")
    is_festival_list = []
    for i in range(len(festivals_df)):
        val = st.slider(
            f"Is_Festival for {festivals_df['name'].iloc[i]} ({festivals_df['date'].iloc[i].date()})",
            0, 1, 1
        )
        is_festival_list.append(val)

    # Build input features with default values
    festivals_df["Is_Festival"] = is_festival_list
    festivals_df["Month"] = festivals_df["date"].dt.month
    festivals_df["DayOfWeek"] = festivals_df["date"].dt.dayofweek
    festivals_df["Is_Weekend"] = festivals_df["DayOfWeek"].apply(lambda x: 1 if x >= 5 else 0)

    input_df = pd.DataFrame({
        "Is_Festival": festivals_df["Is_Festival"],
        "Month": festivals_df["Month"],
        "DayOfWeek": festivals_df["DayOfWeek"],
        "Is_Weekend": festivals_df["Is_Weekend"],
        "Fuel_Price": default_features["Fuel_Price"],
        "CPI": default_features["CPI"],
        "Unemployment": default_features["Unemployment"],
        "Temperature": default_features["Temperature"]
    })

    predictions = model.predict(input_df)
    festivals_df["Predicted_Sales"] = predictions

    st.subheader("📊 Predicted Sales for Upcoming Festivals")
    st.dataframe(festivals_df[["date", "name", "Is_Festival", "Predicted_Sales"]])
    st.line_chart(festivals_df.set_index("date")["Predicted_Sales"])

else:
    st.warning("⚠️ No upcoming national festivals found for the selected country.")