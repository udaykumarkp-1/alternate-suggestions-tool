import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Search Alternate Products", layout="wide")

st.title("🔍 Search Alternate Products")

query = st.text_input("Enter Salt / Product Name")

if query:

    try:
        res = requests.get("http://localhost:8000/search", params={"q": query})

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
        st.error(str(e))