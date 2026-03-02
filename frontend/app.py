import streamlit as st

# UI
from ui.styles import load_styles
from ui.layout import render_header, sidebar

# Services
from services.api import check_has_data

# Components
from components.upload_section import upload_section
from components.search_section import search_section


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Alternate Suggestions Tool",
    page_icon="📊",
    layout="wide"
)

load_styles()
sidebar()
render_header()

# ---------------- CENTERED CONTENT ----------------
left, center, right = st.columns([1, 2, 1])

with center:

    HAS_DATA = check_has_data()

    if HAS_DATA:
        search_section()

    upload_section()

    st.markdown("---")
    st.markdown(
        """
        <p style='text-align:center;font-size:12px; color:#6B7280;'>
        Alternate Suggestions Tool | Version 1.1 | Built by (Uday Kumar.K.P)
        </p>
        """,
        unsafe_allow_html=True
    )