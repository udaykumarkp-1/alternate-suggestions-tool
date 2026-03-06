import streamlit as st


def sidebar():
    st.sidebar.title("Alternate Suggestions Tool")
    st.sidebar.caption("Automated UFM Mapping Engine")

    with st.sidebar.expander("📘 Instructions", expanded=True):
        st.markdown("""
### Supported Files

✔ Excel (.xlsx)  
✔ CSV (.csv)
---
                    
### Format
#### Sheet 1: `Salt + Strength List`
Required Columns:
- Salt + Strength  
- Item Name  
- Qty sold  

#### Sheet 2: `Salt + Strength(Mapped List)`
Required Columns:
- Salt + Strength  

⚠ Column names must be EXACT.
""")


def render_header():

    # Logo at top
    st.markdown("""
        <div class="top-logo">
            <img src="https://www.mrmed.in/nav/nav_logo.svg">
        </div>
    """, unsafe_allow_html=True)

    # Title + Caption
    st.markdown("""
        <div class="header-title">
            Alternate Suggestions Tool
        </div>
    
    """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)