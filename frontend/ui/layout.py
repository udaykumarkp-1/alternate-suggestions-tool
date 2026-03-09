import streamlit as st


# ---------------- SIDEBAR ----------------

def render_sidebar():

    with st.sidebar:

        # LOGO
        st.image(
            "https://www.mrmed.in/nav/nav_logo.svg",
            width=280
        )


        st.markdown("### Navigation")

        st.markdown("🔎 Search Products")
        st.markdown("📤 Bulk Upload")
        st.markdown("📜 History")

        st.markdown("---")

        st.markdown("### File Format Guide")

        st.markdown("**Salt + Strength List**")

        st.markdown("""
- Salt + Strength  
- Item Name  
- Qty sold
""")

        st.markdown("**Salt + Strength (Mapped List)**")

        st.markdown("""
- Salt + Strength
""")

        st.warning("Column names must match exactly.")


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