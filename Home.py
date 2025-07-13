
import streamlit as st
import base64
import os

# ───────────────────────────────────────────────
# PAGE CONFIG
st.set_page_config(
    page_title="StockShield: Smart Inventory Meets Local Intelligence.",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ───────────────────────────────────────────────
# STYLING
st.markdown("""
    <style>
    html, body, [data-testid="stApp"] {
        background-color: #e3f2fd;
        font-family: 'Segoe UI', sans-serif;
    }

    .logo-title-container {
        text-align: center;
        margin-top: 20px;
        margin-bottom: 40px;
    }

    .dashboard-title {
        font-size: 48px;
        font-weight: 800;
        color: #0d47a1;
        margin-top: 20px;
    }

    .tagline {
        font-size: 22px;
        color: #333;
        font-style: italic;
        margin-top: 2px;
        margin-bottom: 60px;
    }

    .footer {
        text-align: center;
        font-size: 19px;
        margin-top: 140px;
        color: #666;
    }

    .stButton > button {
        width: 100%;
        height: 200px;
        background-color: #1565c0 !important;
        color: white !important;
        font-size: 35px;
        font-weight: 800;
        border-radius: 20px;
        border: none;
        box-shadow: 2px 2px 15px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
        padding: 20px;
        white-space: pre-line;
        text-align: center;
        line-height: 1.4;
    }

    .stButton > button:hover {
        background-color: #0d47a1 !important;
        transform: scale(1.03);
        box-shadow: 3px 3px 15px rgba(0,0,0,0.3);
    }
    
    .stButton > button::first-line {
    font-size: 40px;
    font-weight: bold;
}

    /* Optional: reduce vertical padding above and below columns */
    section.main > div { padding-top: 1rem; padding-bottom: 2rem; }

    </style>
""", unsafe_allow_html=True)


# ───────────────────────────────────────────────
# LOGO + TITLE + TAGLINE CENTERED
logo_path = "walmart_logo.jpg"
if os.path.exists(logo_path):
    with open(logo_path, "rb") as img_file:
        img_bytes = img_file.read()
        b64 = base64.b64encode(img_bytes).decode()

    st.markdown(
    f"""
    <div class="logo-title-container">
        <div style="
            height: 60px;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
        ">
            <img src="data:image/png;base64,{b64}"
                 style="height: 120px; object-fit: cover; object-position: center top; margin-top: -10px;">
        </div>
        <div class="dashboard-title">StockShield: Smart Inventory Meets Local Intelligence.</div>
        <div class="tagline">From sunshine to street festivals — never miss a demand signal.</div>
    </div>
    """,
    unsafe_allow_html=True
    )

# ───────────────────────────────────────────────
# 3 BUTTONS (Interactive navigation cards)
col1, col2, col3 = st.columns([1, 1, 1], gap="large")

with col1:
    if st.button("🌤️ Weather-Driven Demand\n\nForecast demand shifts driven by temperature, rain, or storms"):
        st.switch_page("pages/weather_ui.py")

with col2:
    if st.button("🎉 Festival Demand Surge\n\nAnticipate shopping spikes around key regional celebrations"):
        st.switch_page("pages/festival_ui.py")

with col3:
    if st.button("🗓️ Nearby Events Forecast\n\nOptimize inventory around concerts, expos, and city-wide events"):
        st.switch_page("localevents_ui.py")

# ───────────────────────────────────────────────
# FOOTER
st.markdown("""
    <div class="footer">
        Built by Mihika, Akansha & Rahul for Walmart Sparkathon '25
    </div>
""", unsafe_allow_html=True)
