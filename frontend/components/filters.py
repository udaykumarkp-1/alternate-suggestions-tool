import streamlit as st
import pandas as pd


def apply_filters(df: pd.DataFrame):

    st.markdown("### Filters")

    salt_filter = st.selectbox(
        "Salt + Strength",
        ["All"] + sorted(df["Salt + Strength"].dropna().unique())
    )

    if salt_filter != "All":
        df = df[df["Salt + Strength"] == salt_filter]

    return df