import streamlit as st
import pandas as pd
from services.api import search_products

def search_section():

    st.markdown("## 🔍 Search Alternate Products")

    query = st.text_input("Enter Salt / Product Name")

    if query:
        try:
            res = search_products(query.strip())

            if res.status_code == 200:
                data = res.json()

                if not data:
                    st.warning("No results found.")
                else:
                    # Convert response to DataFrame directly
                    df = pd.DataFrame(data)

                    st.dataframe(df, use_container_width=True)

            else:
                st.error("Backend error")

        except Exception as e:
            st.error(str(e))