import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Search Alternate Products", layout="wide")

st.title("🔍 Search Alternate Products")

API_URL = "https://alternate-backend.onrender.com"

query = st.text_input("Enter Salt / Product Name")

if query:
    query = query.strip()  # trim whitespace

    try:
        res = requests.get(
            f"{API_URL}/search",
            params={"q": query},
            timeout=30
        )

        if res.status_code == 200:
            data = res.json()

            if len(data) == 0:
                st.warning("No results found.")
            else:
                df = pd.DataFrame(data, columns=[
                    "Salt + Strength",
                    "Alt 1",
                    "Alt 2",
                    "Alt 3"
                ])

                st.dataframe(df, use_container_width=True)

        else:
            st.error("Backend error")

    except Exception as e:
        st.error(f"Connection error: {e}")