import streamlit as st
import pandas as pd


def apply_filters(df: pd.DataFrame):

    st.markdown("### Filters")

    # ---------------- SALT FILTER ----------------
    salt_options = ["All"] + sorted(df["Salt + Strength"].dropna().unique())

    salt_filter = st.selectbox(
        "Salt + Strength",
        salt_options
    )

    # ---------------- DOSAGE FILTER ----------------
    dosage_options = ["All"]

    if "Dosage Form" in df.columns:
        dosage_values = df["Dosage Form"].dropna().unique().tolist()
        dosage_options += sorted(dosage_values)

    dosage_filter = st.selectbox(
        "Dosage Form",
        dosage_options
    )

    # ---------------- APPLY FILTERS ----------------
    if salt_filter != "All":
        df = df[df["Salt + Strength"] == salt_filter]

    if dosage_filter != "All":
        df = df[df["Dosage Form"] == dosage_filter]

    return df