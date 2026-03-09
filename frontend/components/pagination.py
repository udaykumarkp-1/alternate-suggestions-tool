import streamlit as st
import pandas as pd


def paginate_dataframe(df: pd.DataFrame, rows_per_page: int = 15):

    if df.empty:
        return df

    total_rows = len(df)
    total_pages = (total_rows // rows_per_page) + (1 if total_rows % rows_per_page > 0 else 0)

    if "page_number" not in st.session_state:
        st.session_state.page_number = 1

    page_number = st.session_state.page_number

    # Navigation buttons
    col1, col2, col3 = st.columns([1,2,1])

    with col1:
        if st.button("⬅ Previous") and page_number > 1:
            st.session_state.page_number -= 1

    with col3:
        if st.button("Next ➡") and page_number < total_pages:
            st.session_state.page_number += 1

    page_number = st.session_state.page_number

    st.markdown(
        f"<p style='text-align:center;font-size:12px;color:#6B7280'>Page {page_number} of {total_pages}</p>",
        unsafe_allow_html=True
    )

    start_idx = (page_number - 1) * rows_per_page
    end_idx = start_idx + rows_per_page

    paginated_df = df.iloc[start_idx:end_idx].reset_index(drop=True)

    return paginated_df