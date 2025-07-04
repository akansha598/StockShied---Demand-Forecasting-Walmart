import streamlit as st
import pandas as pd
import numpy as np
import joblib
import requests
from datetime import datetime

# Load trained model
model = joblib.load('weather_model.pkl')

# Fixed/default feature values (mean or latest values)
default_features = {
    "Holiday_Flag": 0,
    "Fuel_Price": 3.25,
    "CPI": 211.5,
    "Unemployment": 7.5
}

# Fetch weather forecast from Visual Crossing
def fetch_weather_forecast(location="Dallas,TX"):
    KEY = ""
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/next7days?unitGroup=metric&include=days&key={KEY}&contentType=json"
    res = requests.get(url)
    data = res.json()
    df = pd.DataFrame(data['days'])[['datetime', 'temp']]
    df.columns = ['Date', 'Temperature']
    df['Date'] = pd.to_datetime(df['Date'])
    return df

# ─────────────────────────────────────────────────────────────────────────────
# Streamlit UI

st.title("🛍️ Walmart Demand Forecast: What-If Weather Impact")
st.markdown("Predict how temperature affects sales using live weather forecast or custom values.")

location = st.text_input("📍 Enter Location (e.g., Dallas,TX):", value="Dallas,TX")

if location:
    forecast_df = fetch_weather_forecast(location)
    st.success("✅ Weather forecast loaded!")
    
    st.subheader("🎛️ Adjust Forecasted Temperature (What-If Simulation)")
    adjusted_temps = []
    for i in range(len(forecast_df)):
        temp = st.slider(
            label=forecast_df['Date'].iloc[i].strftime('%A %d %b'),
            min_value=0.0, max_value=50.0,
            value=float(forecast_df['Temperature'].iloc[i])
        )
        adjusted_temps.append(temp)

    # Add time-based features from forecast dates
    forecast_df['Month'] = forecast_df['Date'].dt.month
    forecast_df['DayOfWeek'] = forecast_df['Date'].dt.dayofweek
    forecast_df['Is_Weekend'] = forecast_df['DayOfWeek'].apply(lambda x: 1 if x >= 5 else 0)
    
    # Build full input for model
    input_data = pd.DataFrame({
        'Temperature': adjusted_temps,
        'Fuel_Price': default_features['Fuel_Price'],
        'CPI': default_features['CPI'],
        'Unemployment': default_features['Unemployment'],
        'Holiday_Flag': default_features['Holiday_Flag'],
        'Month': forecast_df['Month'],
        'DayOfWeek': forecast_df['DayOfWeek'],
        'Is_Weekend': forecast_df['Is_Weekend']
    })
    
    # Predict sales
    predictions = model.predict(input_data)
    forecast_df['Adjusted_Temp'] = adjusted_temps
    forecast_df['Predicted_Sales'] = predictions

    st.subheader("📈 Forecasted Sales Based on Adjusted Temperature")
    st.dataframe(forecast_df[['Date', 'Adjusted_Temp', 'Predicted_Sales']])

    st.line_chart(forecast_df.set_index('Date')['Predicted_Sales'])