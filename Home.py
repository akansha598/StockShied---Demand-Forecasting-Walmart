# import streamlit as st

# # Set page config
# st.set_page_config(
#     page_title="Walmart Forecast Dashboard",
#     layout="centered"
# )

# # Inject custom CSS for styling
# st.markdown("""
#     <style>
#         body {
#             background-color: #e6f2ff;
#         }
#         .main-container {
#             display: flex;
#             flex-direction: column;
#             align-items: center;
#             justify-content: center;
#             height: 80vh;
#         }
#         .button {
#             background-color: #004080;
#             color: white;
#             padding: 1.5em 3em;
#             margin: 1em;
#             font-size: 20px;
#             border: none;
#             border-radius: 10px;
#             text-align: center;
#             width: 300px;
#             cursor: pointer;
#         }
#         .button:hover {
#             background-color: #0059b3;
#         }
#         .logo-container {
#             position: absolute;
#             top: 10px;
#             right: 20px;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # Walmart logo (top right)
# st.markdown("""
#     <div class="logo-container">
#         <img src="assets/walmart_logo.jpg" width="150">
#     </div>
# """, unsafe_allow_html=True)

# # Dashboard content
# st.markdown('<div class="main-container">', unsafe_allow_html=True)

# # Buttons
# col1, col2 = st.columns(2, gap="large")

# with col1:
#     if st.button("🌤️ Weather Forecast", key="weather", help="Go to Weather Forecast"):
#         st.switch_page("pages/weather_ui.py")

# with col2:
#     if st.button("🎉 Festival Forecast", key="festival", help="Go to Festival Forecast"):
#         st.switch_page("pages/festival_ui.py")

# st.markdown("</div>", unsafe_allow_html=True)

# import streamlit as st
# from streamlit_extras.switch_page_button import switch_page
# import base64

# # ─────────────────────────────────────────────────────────────────────────────
# # PAGE CONFIG
# st.set_page_config(
#     page_title="Walmart Forecast Dashboard",
#     layout="centered",
#     initial_sidebar_state="collapsed"
# )

# # ─────────────────────────────────────────────────────────────────────────────
# # STYLE: BACKGROUND + CENTERING
# st.markdown("""
#     <style>
#     body {
#         background-color: #e3f2fd;
#     }
#     .main {
#         background-color: #e3f2fd;
#     }
#     .logo {
#         position: fixed;
#         top: 10px;
#         left: 10px;
#         width: 100px;
#     }
#     .button-container {
#         display: flex;
#         flex-direction: column;
#         align-items: center;
#         justify-content: center;
#         height: 80vh;
#     }
#     .stButton>button {
#         background-color: #1565c0;
#         color: white;
#         font-size: 20px;
#         padding: 20px 40px;
#         margin: 20px;
#         border-radius: 12px;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # ─────────────────────────────────────────────────────────────────────────────
# # LOGO DISPLAY (TOP-LEFT)
# logo_path = "walmart_logo.jpg"
# with open(logo_path, "rb") as img_file:
#     img_bytes = img_file.read()
#     b64 = base64.b64encode(img_bytes).decode()
#     st.markdown(
#         f"<img class='logo' src='data:image/png;base64,{b64}'>",
#         unsafe_allow_html=True
#     )

# # ─────────────────────────────────────────────────────────────────────────────
# # CENTERED BUTTONS
# st.markdown("<div class='button-container'>", unsafe_allow_html=True)

# if st.button("🌤️ Weather Forecast"):
#     switch_page("pages/weather_ui.py")

# if st.button("🎉 Festival Forecast"):
#     switch_page("pages/festival_ui.py")

# st.markdown("</div>", unsafe_allow_html=True)



import streamlit as st
import base64

# ─────────────────────────────────────────────────────────────────────────────
# PAGE CONFIG
st.set_page_config(
    page_title="Walmart Forecast Dashboard",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ─────────────────────────────────────────────────────────────────────────────
# STYLE: BACKGROUND + CENTERING
st.markdown("""
    <style>
    .stApp {
        background-color: #e3f2fd;
    }
    .logo {
        position: fixed;
        top: 10px;
        left: 10px;
        width: 100px;
        z-index: 9999;
    }
    .button-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 80vh;
    }
    .stButton>button {
        background-color: #1565c0;
        color: white;
        font-size: 20px;
        padding: 20px 40px;
        margin: 20px;
        border-radius: 12px;
        width: 300px;
    }
    </style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# LOGO DISPLAY (TOP-LEFT)
logo_path = "walmart_logo.jpg"  # Make sure this is placed in root directory
with open(logo_path, "rb") as img_file:
    img_bytes = img_file.read()
    b64 = base64.b64encode(img_bytes).decode()
    st.markdown(
        f"<img class='logo' src='data:image/png;base64,{b64}'>",
        unsafe_allow_html=True
    )

# ─────────────────────────────────────────────────────────────────────────────
# BUTTON LINKS (official navigation method)
st.markdown("<div class='button-container'>", unsafe_allow_html=True)

st.page_link("pages/weather_ui.py", label="🌤️ Weather Forecast", icon="🌦️")
st.page_link("pages/festival_ui.py", label="🎉 Festival Forecast", icon="🎊")

st.markdown("</div>", unsafe_allow_html=True)
