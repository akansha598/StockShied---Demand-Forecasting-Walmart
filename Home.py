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
# import streamlit as st
# import base64
# from pathlib import Path


# # ───────────────────────────────────────────────────────
# # PAGE CONFIG
# st.set_page_config(
#     page_title="Walmart Forecast Dashboard",
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )

# # ───────────────────────────────────────────────────────
# # LOAD & SHOW LOGO (top-left)

# logo_path = "walmart_logo.jpg"
# if Path(logo_path).exists():
#     with open(logo_path, "rb") as img_file:
#         img_bytes = img_file.read()
#         b64 = base64.b64encode(img_bytes).decode()
#         st.markdown(f"""
#             <div style="position: fixed; top: 20px; left: 20px; z-index: 999;">
#                 <img src="data:image/png;base64,{b64}" width="100">
#             </div>
#         """, unsafe_allow_html=True)
# else:
#     st.warning("⚠️ Logo not found. Please upload 'walmart_logo.jpg' to your repo.")


# # ───────────────────────────────────────────────────────
# # BACKGROUND COLOR
# st.markdown("""
#     <style>
#     .main {
#         background-color: #e3f2fd;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # ───────────────────────────────────────────────────────
# # CENTERED BUTTONS USING COLUMNS

# # Add spacing above
# st.write("")
# st.write("")
# st.write("")
# st.write("")
# st.write("")
# st.write("")

# # Create three columns and center everything in the middle one
# col1, col2, col3 = st.columns([1, 2, 1])
# with col2:
#     st.markdown("<h1 style='text-align: center;'>📊 Walmart Forecast Dashboard</h1>", unsafe_allow_html=True)
#     st.write("##")
#     if st.button("🌤️  Weather Forecast", use_container_width=True):
#         st.switch_page("pages/weather_ui.py")
#     st.write("")
#     if st.button("🎉  Festival Forecast", use_container_width=True):
#         st.switch_page("pages/festival_ui.py")
# import streamlit as st
# import base64
# import os

# # ───────────────────────────────────────────────────────
# # PAGE CONFIG
# st.set_page_config(
#     page_title="Walmart Forecast Dashboard",
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )

# # ───────────────────────────────────────────────────────
# # BACKGROUND COLOR OVERRIDE + LOGO FIX
# st.markdown("""
#     <style>
#     html, body, [data-testid="stApp"] {
#         background-color: #e3f2fd !important;
#     }
#     .logo-container {
#         position: fixed;
#         top: 20px;
#         left: 20px;
#         z-index: 9999;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # ───────────────────────────────────────────────────────
# # LOGO DISPLAY (TOP-LEFT WITH FALLBACK)
# logo_path = "walmart_logo.jpg"
# if os.path.exists(logo_path):
#     with open(logo_path, "rb") as img_file:
#         img_bytes = img_file.read()
#         b64 = base64.b64encode(img_bytes).decode()

#     st.markdown(
#         f"""
#         <div class="logo-container">
#             <img src="data:image/png;base64,{b64}" width="100">
#         </div>
#         """,
#         unsafe_allow_html=True
#     )
# else:
#     st.warning("🔍 Logo file not found. Please make sure 'walmart_logo.jpg' is in the project folder.")

# # ───────────────────────────────────────────────────────
# # CENTERED BUTTONS USING COLUMNS

# st.write("")
# st.write("")
# st.write("")

# col1, col2, col3 = st.columns([1, 2, 1])
# with col2:
#     st.markdown("<h1 style='text-align: center;'>📊 Walmart Forecast Dashboard</h1>", unsafe_allow_html=True)
#     st.write("##")
#     if st.button("🌤️  Weather Forecast", use_container_width=True):
#         st.switch_page("pages/weather_ui.py")
#     st.write("")
#     if st.button("🎉  Festival Forecast", use_container_width=True):
#         st.switch_page("pages/festival_ui.py")
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
# # BACKGROUND COLOR OVERRIDE
# # st.markdown("""
# #     <style>
# #     html, body, [data-testid="stApp"] {
# #         background-color: #e3f2fd !important;
# #     }

# #     .logo-container {
# #         position: fixed;
# #         top: 20px;
# #         left: 20px;
# #         z-index: 9999;
# #     }

# #     .stButton > button {
# #         background-color: #1565c0;
# #         color: white;
# #         font-size: 20px;
# #         width: 200px;
# #         height: 200px;
# #         border-radius: 12px;
# #         font-weight: bold;
# #     }

# #     .centered {
# #         display: flex;
# #         justify-content: center;
# #         align-items: center;
# #         height: 75vh;
# #         gap: 50px;
# #     }
# #     </style>
# # """, unsafe_allow_html=True)


# st.markdown("""
#     <style>
#     .button-container {
#         background-color: #e3f2fd;
#         padding: 50px;
#         border-radius: 20px;
#         text-align: center;
#     }
#     .square-button {
#         background-color: #1565c0;
#         color: white;
#         font-size: 20px;
#         padding: 40px 40px;
#         border-radius: 12px;
#         width: 200px;
#         height: 200px;
#         margin: 30px;
#         display: inline-block;
#         text-align: center;
#         vertical-align: middle;
#     }
#     .square-button:hover {
#         background-color: #0d47a1;
#     }
#     </style>
# """, unsafe_allow_html=True)
# # ───────────────────────────────────────────────
# # OPTIONAL LOGO DISPLAY (TOP-LEFT)
# logo_path = "walmart_logo.jpg"
# if os.path.exists(logo_path):
#     with open(logo_path, "rb") as img_file:
#         img_bytes = img_file.read()
#         b64 = base64.b64encode(img_bytes).decode()

#     st.markdown(
#         f"""
#         <div class="logo-container">
#             <img src="data:image/png;base64,{b64}" width="80" height="80">
#         </div>
#         """,
#         unsafe_allow_html=True
#     )

# # ───────────────────────────────────────────────
# # DASHBOARD TITLE
# st.markdown("<h1 style='text-align: center;'>📊 Walmart Forecast Dashboard</h1>", unsafe_allow_html=True)

# # ───────────────────────────────────────────────
# # TWO SQUARE BUTTONS CENTERED HORIZONTALLY
# st.markdown("<div class='centered'>", unsafe_allow_html=True)

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
    }

    .logo-title-container {
        text-align: center;
        margin-top: 30px;
        margin-bottom: 10px;
    }

    .dashboard-title {
        font-size: 40px;
        font-weight: bold;
        color: #0d47a1;
        margin-top: 10px;
    }

    .button-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 60px;
        gap: 60px;
    }

    .stButton > button {
        width: 200px;
        height: 200px;
        background-color: #1565c0;
        color: white;
        font-size: 18px;
        border-radius: 20px;
        font-weight: bold;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
    }

    .stButton > button:hover {
        background-color: #0d47a1;
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

# ───────────────────────────────────────────────
# LOGO + TITLE CENTERED TOGETHER
logo_path = "walmart_logo.jpg"
if os.path.exists(logo_path):
    with open(logo_path, "rb") as img_file:
        img_bytes = img_file.read()
        b64 = base64.b64encode(img_bytes).decode()

    st.markdown(
        f"""
        <div class="logo-title-container">
            <img src="data:image/png;base64,{b64}" width="100">
            <div class="dashboard-title">📊 Walmart Forecast Dashboard</div>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown("<h1 style='text-align: center;'>📊 Walmart Forecast Dashboard</h1>", unsafe_allow_html=True)

# ───────────────────────────────────────────────
# TWO BIG SQUARE BUTTONS CENTERED
st.markdown("<div class='button-container'>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])
with col1:
    if st.button("🌤️ Weather Forecast"):
        st.switch_page("pages/weather_ui.py")
with col2:
    if st.button("🎉 Festival Forecast"):
        st.switch_page("pages/festival_ui.py")

st.markdown("</div>", unsafe_allow_html=True)
