



# import streamlit as st
# import base64
# import os

# # ───────────────────────────────────────────────
# # PAGE CONFIG
# st.set_page_config(
#     page_title="Walmart Forecast Dashboard",
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )

# # ───────────────────────────────────────────────
# # BACKGROUND COLOR & STYLING
# st.markdown("""
#     <style>
#     html, body, [data-testid="stApp"] {
#         background-color: #e3f2fd;
#     }

#     .button-row {
#         display: flex;
#         justify-content: center;
#         align-items: center;
#         gap: 50px;
#         margin-top: 50px;
#     }

#     .stButton > button {
#         background-color: #1565c0;
#         color: white;
#         font-size: 18px;
#         width: 200px;
#         height: 200px;
#         border-radius: 16px;
#         font-weight: bold;
#         transition: background-color 0.3s ease;
#     }

#     .stButton > button:hover {
#         background-color: #0d47a1;
#     }

#     .logo-title {
#         display: flex;
#         align-items: center;
#         justify-content: center;
#         gap: 20px;
#         margin-bottom: 20px;
#         margin-top: 30px;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # ───────────────────────────────────────────────
# # WALMART LOGO + TITLE
# st.markdown("<div class='logo-title'>", unsafe_allow_html=True)

# col1, col2, col3 = st.columns([2, 6, 2])
# with col2:
#     # Logo + Title side by side
#     st.markdown("<div style='display: flex; align-items: center; justify-content: center; gap: 20px;'>", unsafe_allow_html=True)

#     logo_path = "walmart_logo.jpg"
#     if os.path.exists(logo_path):
#         with open(logo_path, "rb") as img_file:
#             img_bytes = img_file.read()
#             b64 = base64.b64encode(img_bytes).decode()
#         st.markdown(
#             f"<img src='data:image/png;base64,{b64}' width='80' height='80'>",
#             unsafe_allow_html=True
#         )

#     st.markdown("<h1>📊 Walmart Forecast Dashboard</h1>", unsafe_allow_html=True)
#     st.markdown("</div>", unsafe_allow_html=True)

# st.markdown("</div>", unsafe_allow_html=True)

# # ───────────────────────────────────────────────
# # BUTTONS SECTION
# st.markdown("<div class='button-row'>", unsafe_allow_html=True)

# col1, col2, col3 = st.columns([1, 1, 1])
# with col1:
#     if st.button("🌤️ Weather Forecast"):
#         st.switch_page("pages/weather_ui.py")
# with col2:
#     if st.button("🎉 Festival Forecast"):
#         st.switch_page("pages/festival_ui.py")

# st.markdown("</div>", unsafe_allow_html=True)



# import streamlit as st
# import base64
# import os

# # ───────────────────────────────────────────────
# # PAGE CONFIG
# st.set_page_config(
#     page_title="Walmart Forecast Dashboard",
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )

# # ───────────────────────────────────────────────
# # STYLING: Background, Buttons, Logo
# st.markdown("""
#     <style>
#     html, body, [data-testid="stApp"] {
#         background-color: #e3f2fd;
#     }

#     .logo {
#         position: fixed;
#         top: 20px;
#         left: 30px;
#         z-index: 9999;
#     }

#     .dashboard-title {
#         text-align: center;
#         font-size: 40px;
#         font-weight: bold;
#         margin-top: 50px;
#         color: #0d47a1;
#     }

#     .button-container {
#         display: flex;
#         justify-content: center;
#         align-items: center;
#         margin-top: 80px;
#         gap: 60px;
#     }

#     .stButton > button {
#         width: 200px;
#         height: 200px;
#         background-color: #1565c0;
#         color: white;
#         font-size: 18px;
#         border-radius: 20px;
#         font-weight: bold;
#         box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
#         transition: all 0.3s ease;
#     }

#     .stButton > button:hover {
#         background-color: #0d47a1;
#         transform: scale(1.05);
#     }
#     </style>
# """, unsafe_allow_html=True)

# # ───────────────────────────────────────────────
# # LOGO (top-left corner)
# logo_path = "walmart_logo.jpg"
# if os.path.exists(logo_path):
#     with open(logo_path, "rb") as img_file:
#         img_bytes = img_file.read()
#         b64 = base64.b64encode(img_bytes).decode()
#     st.markdown(
#         f"""
#         <div class="logo">
#             <img src="data:image/png;base64,{b64}" width="100">
#         </div>
#         """,
#         unsafe_allow_html=True
#     )

# # ───────────────────────────────────────────────
# # DASHBOARD TITLE
# st.markdown("<div class='dashboard-title'>📊 Walmart Forecast Dashboard</div>", unsafe_allow_html=True)

# # ───────────────────────────────────────────────
# # TWO BIG SQUARE BUTTONS CENTERED
# st.markdown("<div class='button-container'>", unsafe_allow_html=True)

# col1, col2 = st.columns([1, 1])
# with col1:
#     if st.button("🌤️ Weather Forecast"):
#         st.switch_page("pages/weather_ui.py")
# with col2:
#     if st.button("🎉 Festival Forecast"):
#         st.switch_page("pages/festival_ui.py")

# st.markdown("</div>", unsafe_allow_html=True)




# import streamlit as st
# import base64
# import os

# # ───────────────────────────────────────────────
# # PAGE CONFIG
# st.set_page_config(
#     page_title="Walmart Forecast Dashboard",
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )

# # ───────────────────────────────────────────────
# # STYLING
# st.markdown("""
#     <style>
#     html, body, [data-testid="stApp"] {
#         background-color: #e3f2fd;
#     }

#     .logo-title-container {
#         text-align: center;
#         margin-top: 30px;
#         margin-bottom: 10px;
#     }

#     .dashboard-title {
#         font-size: 40px;
#         font-weight: bold;
#         color: #0d47a1;
#         margin-top: 10px;
#     }

#     .button-container {
#         display: flex;
#         justify-content: center;
#         align-items: center;
#         margin-top: 60px;
#         gap: 60px;
#     }

#     .stButton > button {
#         width: 200px;
#         height: 200px;
#         background-color: #1565c0 !important;
#         color: white !important;
#         font-size: 18px;
#         border-radius: 20px;
#         font-weight: bold;
#         box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
#         transition: all 0.3s ease;
#         border: none;
#     }

#     .stButton > button:hover,
#     .stButton > button:focus,
#     .stButton > button:active {
#         background-color: #0d47a1 !important;
#         color: white !important;
#         outline: none !important;
#         box-shadow: 2px 2px 10px rgba(0,0,0,0.3);
#     }
#     </style>
# """, unsafe_allow_html=True)


# # ───────────────────────────────────────────────
# # LOGO + TITLE CENTERED TOGETHER
# logo_path = "walmart_logo.jpg"
# if os.path.exists(logo_path):
#     with open(logo_path, "rb") as img_file:
#         img_bytes = img_file.read()
#         b64 = base64.b64encode(img_bytes).decode()

#     st.markdown(
#         f"""
#         <div class="logo-title-container">
#             <img src="data:image/png;base64,{b64}" width="200">
#             <div class="dashboard-title">📊 Walmart Forecast Dashboard</div>
#         </div>
#         """,
#         unsafe_allow_html=True
#     )
# else:
#     st.markdown("<h1 style='text-align: center;'>📊 Walmart Forecast Dashboard</h1>", unsafe_allow_html=True)

# # ───────────────────────────────────────────────
# # TWO BIG SQUARE BUTTONS CENTERED
# st.markdown("<div class='button-container'>", unsafe_allow_html=True)

# col1, col2 = st.columns([1, 1])
# with col1:
#     if st.button("🌤️ Weather Forecast"):
#         st.switch_page("pages/weather_ui.py")
# with col2:
#     if st.button("🎉 Festival Forecast"):
#         st.switch_page("pages/festival_ui.py")

# st.markdown("</div>", unsafe_allow_html=True)














# import streamlit as st
# import base64
# import os

# # ───────────────────────────────────────────────
# # PAGE CONFIG
# st.set_page_config(
#     page_title="Walmart Forecast Dashboard",
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )

# # ───────────────────────────────────────────────
# # STYLING
# st.markdown("""
#     <style>
#     html, body, [data-testid="stApp"] {
#         background-color: #e3f2fd;
#     }

#     .logo-title-container {
#         text-align: center;
#         margin-top: 30px;
#         margin-bottom: 10px;
#     }

#     .dashboard-title {
#         font-size: 40px;
#         font-weight: bold;
#         color: #0d47a1;
#         margin-top: 10px;
#     }

#     .tagline {
#         font-size: 20px;
#         color: #333;
#         font-style: italic;
#         margin-top: 10px;
#         margin-bottom: 30px;
#     }

#     .button-container {
#         display: flex;
#         justify-content: center;
#         align-items: center;
#         margin-top: 60px;
#         gap: 60px;
#     }

#     .stButton > button {
#         width: 200px;
#         height: 200px;
#         background-color: #1565c0 !important;
#         color: white !important;
#         font-size: 18px;
#         border-radius: 20px;
#         font-weight: bold;
#         box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
#         transition: all 0.3s ease;
#         border: none;
#     }

#     .stButton > button:hover,
#     .stButton > button:focus,
#     .stButton > button:active {
#         background-color: #0d47a1 !important;
#         color: white !important;
#         outline: none !important;
#         box-shadow: 2px 2px 10px rgba(0,0,0,0.3);
#     }
#     </style>
# """, unsafe_allow_html=True)

# # ───────────────────────────────────────────────
# # LOGO + TITLE + TAGLINE CENTERED
# logo_path = "walmart_logo.jpg"
# if os.path.exists(logo_path):
#     with open(logo_path, "rb") as img_file:
#         img_bytes = img_file.read()
#         b64 = base64.b64encode(img_bytes).decode()

#     st.markdown(
#         f"""
#         <div class="logo-title-container">
#             <img src="data:image/png;base64,{b64}" width="200">
#             <div class="dashboard-title">📊 Walmart Forecast Dashboard</div>
#             <div class="tagline">Empowering smarter inventory decisions with hyperlocal insights</div>
#         </div>
#         """,
#         unsafe_allow_html=True
#     )
# else:
#     st.markdown("""
#         <div class="logo-title-container">
#             <div class="dashboard-title">📊 Walmart Forecast Dashboard</div>
#             <div class="tagline">Empowering smarter inventory decisions with hyperlocal insights</div>
#         </div>
#     """, unsafe_allow_html=True)

# # ───────────────────────────────────────────────
# # BUTTONS
# st.markdown("<div class='button-container'>", unsafe_allow_html=True)

# col1, col2 = st.columns([1, 1])
# with col1:
#     if st.button("🌤️ Weather Forecast"):
#         st.switch_page("pages/weather_ui.py")
# with col2:
#     if st.button("🎉 Festival Forecast"):
#         st.switch_page("pages/festival_ui.py")

# st.markdown("</div>", unsafe_allow_html=True)





# import streamlit as st
# import base64
# import os

# # ───────────────────────────────────────────────
# # PAGE CONFIG
# st.set_page_config(
#     page_title="Walmart Forecast Dashboard",
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )

# # ───────────────────────────────────────────────
# # STYLING
# st.markdown("""
#     <style>
#     html, body, [data-testid="stApp"] {
#         background-color: #e3f2fd;
#     }

#     .logo-title-container {
#         text-align: center;
#         margin-top: 30px;
#         margin-bottom: 10px;
#     }

#     .dashboard-title {
#         font-size: 42px;
#         font-weight: bold;
#         color: #0d47a1;
#         margin-top: 10px;
#     }

#     .tagline {
#         font-size: 20px;
#         color: #333;
#         font-style: italic;
#         margin-top: 5px;
#         margin-bottom: 40px;
#     }

#     .button-container {
#         display: flex;
#         justify-content: center;
#         align-items: center;
#         gap: 80px;
#         margin-top: 60px;
#     }

#     .custom-btn {
#         width: 220px;
#         height: 200px;
#         background-color: #1565c0 !important;
#         color: white !important;
#         font-size: 20px;
#         border-radius: 20px;
#         font-weight: bold;
#         box-shadow: 3px 3px 15px rgba(0,0,0,0.2);
#         transition: all 0.3s ease;
#         border: none;
#         text-align: center;
#         padding-top: 25px;
#     }

#     .custom-btn:hover {
#         background-color: #0d47a1 !important;
#         transform: scale(1.03);
#         box-shadow: 3px 3px 15px rgba(0,0,0,0.3);
#     }

#     .custom-subtext {
#         font-size: 14px;
#         font-weight: normal;
#         color: #f0f0f0;
#         margin-top: 10px;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # ───────────────────────────────────────────────
# # LOGO + TITLE + TAGLINE CENTERED
# logo_path = "walmart_logo.jpg"
# if os.path.exists(logo_path):
#     with open(logo_path, "rb") as img_file:
#         img_bytes = img_file.read()
#         b64 = base64.b64encode(img_bytes).decode()

#     st.markdown(
#         f"""
#         <div class="logo-title-container">
#             <img src="data:image/png;base64,{b64}" width="200">
#             <div class="dashboard-title">📊 Walmart Forecast Dashboard</div>
#             <div class="tagline">Empowering smarter inventory decisions with hyperlocal insights</div>
#         </div>
#         """,
#         unsafe_allow_html=True
#     )
# else:
#     st.markdown("""
#         <div class="logo-title-container">
#             <div class="dashboard-title">📊 Walmart Forecast Dashboard</div>
#             <div class="tagline">Empowering smarter inventory decisions with hyperlocal insights</div>
#         </div>
#     """, unsafe_allow_html=True)

# # ───────────────────────────────────────────────
# # BUTTONS AS HTML SO THEY CAN BE STYLED
# st.markdown("<div class='button-container'>", unsafe_allow_html=True)

# col1, col2 = st.columns(2)

# with col1:
#     if st.button("🌤️ Weather Forecast\n\nPredict demand using rain/temp", key="weather"):
#         st.switch_page("pages/weather_ui.py")
# with col2:
#     if st.button("🎉 Festival Forecast\n\nSee surges due to local events", key="festival"):
#         st.switch_page("pages/festival_ui.py")

# st.markdown("</div>", unsafe_allow_html=True)



# import streamlit as st
# import base64
# import os

# # ───────────────────────────────────────────────
# # PAGE CONFIG
# st.set_page_config(
#     page_title="Walmart Forecast Dashboard",
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )

# # ───────────────────────────────────────────────
# # STYLING
# st.markdown("""
#     <style>
#     html, body, [data-testid="stApp"] {
#         background-color: #e3f2fd;
#         font-family: 'Segoe UI', sans-serif;
#     }

#     .logo-title-container {
#         text-align: center;
#         margin-top: 30px;
#         margin-bottom: 20px;
#     }

#     .dashboard-title {
#         font-size: 42px;
#         font-weight: 700;
#         color: #0d47a1;
#         margin-top: 15px;
#     }

#     .tagline {
#         font-size: 18px;
#         color: #333;
#         margin-top: 5px;
#         font-style: italic;
#     }

#     .forecast-box {
#         background-color: #1565c0;
#         border-radius: 20px;
#         color: white;
#         padding: 40px 20px;
#         text-align: center;
#         font-size: 18px;
#         font-weight: 600;
#         box-shadow: 2px 2px 15px rgba(0,0,0,0.2);
#         transition: all 0.3s ease;
#     }

#     .forecast-box:hover {
#         background-color: #0d47a1;
#         transform: scale(1.03);
#         box-shadow: 3px 3px 15px rgba(0,0,0,0.3);
#     }

#     .forecast-subtext {
#         font-size: 14px;
#         font-weight: normal;
#         color: #e0e0e0;
#         margin-top: 10px;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # ───────────────────────────────────────────────
# # LOGO + TITLE + TAGLINE CENTERED
# logo_path = "walmart_logo.jpg"
# if os.path.exists(logo_path):
#     with open(logo_path, "rb") as img_file:
#         img_bytes = img_file.read()
#         b64 = base64.b64encode(img_bytes).decode()

#     st.markdown(
#         f"""
#         <div class="logo-title-container">
#             <img src="data:image/png;base64,{b64}" width="200">
#             <div class="dashboard-title">Walmart Forecast Dashboard</div>
#             <div class="tagline">Empowering smarter inventory decisions with hyperlocal insights</div>
#         </div>
#         """,
#         unsafe_allow_html=True
#     )
# else:
#     st.markdown("""
#         <div class="logo-title-container">
#             <div class="dashboard-title">Walmart Forecast Dashboard</div>
#             <div class="tagline">Empowering smarter inventory decisions with hyperlocal insights</div>
#         </div>
#     """, unsafe_allow_html=True)

# # ───────────────────────────────────────────────
# # TWO CARDS - WEATHER & FESTIVAL
# col1, col2 = st.columns([1, 1], gap="large")

# with col1:
#     if st.button("🌤️ Weather Forecast"):
#         st.switch_page("pages/weather_ui.py")
#     st.markdown('<div class="forecast-box">🌤️ Weather Forecast<br><span class="forecast-subtext">Predict demand using rain/temp</span></div>', unsafe_allow_html=True)

# with col2:
#     if st.button("🎉 Festival Forecast"):
#         st.switch_page("pages/festival_ui.py")
#     st.markdown('<div class="forecast-box">🎉 Festival Forecast<br><span class="forecast-subtext">See surges due to local events</span></div>', unsafe_allow_html=True)


# import streamlit as st
# import base64
# import os

# st.set_page_config(
#     page_title="Walmart Forecast Dashboard",
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )

# # ───────────────────────────────────────────────
# # STYLING
# st.markdown("""
#     <style>
#     html, body, [data-testid="stApp"] {
#         background-color: #e3f2fd;
#         font-family: 'Segoe UI', sans-serif;
#     }

#     .logo-title-container {
#         text-align: center;
#         margin-top: 30px;
#         margin-bottom: 20px;
#     }

#     .dashboard-title {
#         font-size: 42px;
#         font-weight: 700;
#         color: #0d47a1;
#         margin-top: 15px;
#     }

#     .tagline {
#         font-size: 18px;
#         color: #333;
#         margin-top: 5px;
#         font-style: italic;
#     }

#     .forecast-box {
#         background-color: #1565c0;
#         border-radius: 20px;
#         color: white;
#         padding: 40px 20px;
#         text-align: center;
#         font-size: 18px;
#         font-weight: 600;
#         box-shadow: 2px 2px 15px rgba(0,0,0,0.2);
#         transition: all 0.3s ease;
#         cursor: pointer;
#     }

#     .forecast-box:hover {
#         background-color: #0d47a1;
#         transform: scale(1.03);
#         box-shadow: 3px 3px 15px rgba(0,0,0,0.3);
#     }

#     .forecast-subtext {
#         font-size: 14px;
#         font-weight: normal;
#         color: #e0e0e0;
#         margin-top: 10px;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # ───────────────────────────────────────────────
# # LOGO + TITLE + TAGLINE
# logo_path = "walmart_logo.jpg"
# if os.path.exists(logo_path):
#     with open(logo_path, "rb") as img_file:
#         img_bytes = img_file.read()
#         b64 = base64.b64encode(img_bytes).decode()

#     st.markdown(
#         f"""
#         <div class="logo-title-container">
#             <img src="data:image/png;base64,{b64}" width="200">
#             <div class="dashboard-title">Walmart Forecast Dashboard</div>
#             <div class="tagline">Empowering smarter inventory decisions with hyperlocal insights</div>
#         </div>
#         """,
#         unsafe_allow_html=True
#     )
# else:
#     st.markdown("""
#         <div class="logo-title-container">
#             <div class="dashboard-title">Walmart Forecast Dashboard</div>
#             <div class="tagline">Empowering smarter inventory decisions with hyperlocal insights</div>
#         </div>
#     """, unsafe_allow_html=True)

# # ───────────────────────────────────────────────
# # BLUE CARDS THAT LINK TO PAGES
# col1, col2 = st.columns([1, 1], gap="large")

# with col1:
#     st.markdown(
#         """
#         <a href="/pages/weather_ui" target="_self">
#             <div class="forecast-box">
#                 🌤️ Weather Forecast
#                 <div class="forecast-subtext">Predict demand using rain/temp</div>
#             </div>
#         </a>
#         """, unsafe_allow_html=True
#     )

# with col2:
#     st.markdown(
#         """
#         <a href="/pages/festival_ui" target="_self">
#             <div class="forecast-box">
#                 🎉 Festival Forecast
#                 <div class="forecast-subtext">See surges due to local events</div>
#             </div>
#         </a>
#         """, unsafe_allow_html=True
#     )


import streamlit as st
import base64
import os

# ───────────────────────────────────────────────
# PAGE CONFIG
st.set_page_config(
    page_title="Walmart Forecast Dashboard",
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
        margin-top: 30px;
        margin-bottom: 30px;
    }

    .dashboard-title {
        font-size: 55px;
        font-weight: 700;
        color: #0d47a1;
        margin-top: 15px;
    }

    .tagline {
        font-size: 18px;
        color: #333;
        margin-top: 5px;
        font-style: italic;
    }

    .forecast-container {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 60px;
        margin-top: 50px;
        flex-wrap: wrap;
    }

    .forecast-box {
        background-color: #1565c0;
        border-radius: 20px;
        color: white;
        padding: 40px 25px;
        text-align: center;
        font-size: 20px;
        font-weight: 600;
        width: 280px;
        height: 180px;
        box-shadow: 2px 2px 15px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
        cursor: pointer;
        text-decoration: none;
    }

    .forecast-box:hover {
        background-color: #0d47a1;
        transform: scale(1.05);
        box-shadow: 3px 3px 15px rgba(0,0,0,0.3);
    }

    .forecast-subtext {
        font-size: 14px;
        font-weight: normal;
        color: #e0e0e0;
        margin-top: 12px;
    }

    .footer {
        text-align: center;
        font-size: 13px;
        margin-top: 80px;
        color: #777;
    }

    a {
        text-decoration: none !important;
    }
    
    .forecast-container {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 60px;
    margin-top: 80px;
    flex-wrap: wrap;
}

.forecast-box {
    background-color: #1565c0;
    border-radius: 20px;
    color: white;
    padding: 40px 25px;
    text-align: center;
    font-size: 20px;
    font-weight: 600;
    width: 280px;
    height: 180px;
    box-shadow: 2px 2px 15px rgba(0,0,0,0.2);
    transition: all 0.3s ease;
    cursor: pointer;
    text-decoration: none;
}

    </style>
""", unsafe_allow_html=True)

# ───────────────────────────────────────────────
# LOGO + TITLE
logo_path = "walmart_logo.jpg"
if os.path.exists(logo_path):
    with open(logo_path, "rb") as img_file:
        img_bytes = img_file.read()
        b64 = base64.b64encode(img_bytes).decode()

    # st.markdown(
    #     f"""
    #     <div class="logo-title-container">
    #         <img src="data:image/png;base64,{b64}" width="180">
    #         <div class="dashboard-title">Walmart Forecast Dashboard</div>
    #         <div class="tagline">Empowering smarter inventory decisions with hyperlocal insights</div>
    #     </div>
    #     """,
    #     unsafe_allow_html=True
    # )
    
    st.markdown(
    f"""
    <div class="logo-title-container">
        <div style="
            height: 50px;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
        ">
            <img src="data:image/png;base64,{b64}"
                 style="height: 150px; object-fit: cover; object-position: center top; margin-top: -10px;">
        </div>
        <div class="dashboard-title">Walmart Forecast Dashboard</div>
        <div class="tagline">Empowering smarter inventory decisions with hyperlocal insights</div>
    </div>
    """,
    unsafe_allow_html=True
    )

else:
    st.markdown("""
        <div class="logo-title-container">
            <div class="dashboard-title">Walmart Forecast Dashboard</div>
            <div class="tagline">Empowering smarter inventory decisions with hyperlocal insights</div>
        </div>
    """, unsafe_allow_html=True)

# ───────────────────────────────────────────────
# ───────────────────────────────────────────────
# FORECAST BUTTON CARDS – IN A ROW (FLEX)
st.markdown("""
    <div class="forecast-container">
        <a href="/pages/weather_ui" target="_self">
            <div class="forecast-box">
                🌤️ Weather Forecast
                <div class="forecast-subtext">Predict demand using rain/temp</div>
            </div>
        </a>
        <a href="/pages/festival_ui" target="_self">
            <div class="forecast-box">
                🎉 Festival Forecast
                <div class="forecast-subtext">Plan for festival-based shopping spikes</div>
            </div>
        </a>
        <a href="/pages/events_ui" target="_self">
            <div class="forecast-box">
                📅 Local Event Forecast
                <div class="forecast-subtext">Uplift your stock for upcoming events</div>
            </div>
        </a>
    </div>
""", unsafe_allow_html=True)

# ───────────────────────────────────────────────
# FOOTER
st.markdown("""
    <div class="footer">
        🚀 Built with ❤️ for Walmart Hackathon · Powered by Streamlit
    </div>
""", unsafe_allow_html=True)
