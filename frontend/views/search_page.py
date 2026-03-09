import streamlit as st
import pandas as pd

from components.search_bar import render_search_bar
from components.result_table import render_results_table
from components.filters import apply_filters
from components.pagination import paginate_dataframe

from services.api import search_api


def render_search_page():

    # ---------------- SEARCH BAR ----------------

    query, run_search = render_search_bar()

    if not query:
        return

    # ---------------- SEARCH API ----------------

    if run_search:

        with st.spinner("Searching database..."):

            results = search_api(query)

        if not results:
            st.warning("No results found.")
            return

        df = pd.DataFrame(results)

        st.session_state["search_results"] = df


    # ---------------- LOAD FROM SESSION ----------------

    if "search_results" not in st.session_state:
        return

    df = st.session_state["search_results"]

    # ---------------- FILTERS ----------------

    df = apply_filters(df)

    # ---------------- PAGINATION ----------------

    df_page = paginate_dataframe(df)

    # ---------------- RESULTS HEADER ----------------

    st.markdown(
        f"""
        <div style="
            display:flex;
            justify-content:space-between;
            align-items:center;
            margin-top:20px;
            margin-bottom:10px;
        ">

        <div style="font-weight:600;color:#0D2137">
        {len(df)} Results
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # ---------------- TABLE ----------------

    render_results_table(df_page)

    # ---------------- EXPORT ----------------

    csv = df.to_csv(index=False)

    st.download_button(
        "Export CSV",
        csv,
        "search_results.csv",
        "text/csv"
    )