import streamlit as st

def load_styles():
    st.markdown("""
    <style>

    /* Remove default Streamlit top padding */
    .block-container {
        padding-top: 1rem !important;
    }

    /* ===== TOP LOGO ===== */
    .top-logo {
        margin-top: 27px;
        margin-bottom: 15px;
    }

    .top-logo img {
        max-width: 220px;
        height: auto;
    }

    /* ===== HEADER TEXT ===== */
    .header-title {
        font-size: 42px;
        font-weight: 700;
        margin: 0;
        color: #1F2937;
    }

    .header-caption {
        font-size: 16px;
        color: #6B7280;
        margin-top: 6px;
        margin-bottom: 15px;
    }

    /* ===== MOBILE RESPONSIVE ===== */
    @media (max-width: 768px) {

        .top-logo img {
            max-width: 180px;
        }

        .header-title {
            font-size: 30px;
        }
    }

    /* ===================================================== */
    /* ===== ADDITIONAL SPACING CONTROL (NEW ADDITION) ===== */
    /* ===================================================== */

    /* Reduce spacing between Streamlit sections */
    div.block-container > div {
        margin-bottom: 0.6rem;
    }

    /* Reduce spacing after section headings like Upload File */
    h1, h2, h3 {
        margin-bottom: 0.5rem !important;
    }

    /* Reduce space before file uploader */
    [data-testid="stFileUploader"] {
        margin-top: -8px;
    }

    </style>
    """, unsafe_allow_html=True)