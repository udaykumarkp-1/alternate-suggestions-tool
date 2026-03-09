import streamlit as st

# UI
from ui.styles import load_styles
from ui.layout import render_sidebar, render_header

# Pages
from views.search_page import render_search_page
from views.upload_page import render_upload_page
from views.history_page import render_history_page


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Alternate Suggestions Tool",
    page_icon="💊",
    layout="wide"
)

# ---------------- LOAD GLOBAL STYLES ----------------

load_styles()

# ---------------- SIDEBAR ----------------

render_sidebar()

# ---------------- HEADER ----------------

render_header()

# ---------------- TABS NAVIGATION ----------------

tab1, tab2, tab3 = st.tabs([
    "🔎 Search",
    "📤 Bulk Upload",
    "📜 History"
])

# ---------------- SEARCH PAGE ----------------

with tab1:
    render_search_page()

# ---------------- UPLOAD PAGE ----------------

with tab2:
    render_upload_page()

# ---------------- HISTORY PAGE ----------------

with tab3:
    render_history_page()

