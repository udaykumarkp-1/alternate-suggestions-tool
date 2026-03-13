import streamlit as st


# ---------------- SIDEBAR ----------------

def render_sidebar():
        # LOGO
        st.image(
            "https://www.mrmed.in/nav/nav_logo.svg",
            width=280
        )
# ---------------- HEADER ----------------

def render_header():

    st.markdown("""
<div style="
background:#0D2167;
padding:8px 18px;
border-radius:8px;
margin-bottom:15px;
display:flex;
align-items:center;
justify-content:center;
color:white;
font-size:24px;
font-weight:600;
height:42px;
">

Alternate Suggestions Tool

</div>
""", unsafe_allow_html=True)