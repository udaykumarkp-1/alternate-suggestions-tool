import streamlit as st
import pandas as pd


def apply_filters(df: pd.DataFrame):

    st.markdown("### Filters")

    col1, col2 = st.columns(2)

    # ---------------- SALT FILTER ----------------
    with col1:
        salt_options = ["All"] + sorted(df["Salt + Strength"].dropna().unique().tolist())

        salt_filter = st.selectbox(
            "Salt + Strength",
            salt_options,
            key="salt_filter"
        )

    # ---------------- DOSAGE FILTER — cascades from salt ----------------
    with col2:
        # ✅ FIX: Build dosage options ONLY from rows matching the selected salt
        if salt_filter != "All":
            dosage_source = df[df["Salt + Strength"] == salt_filter]
        else:
            dosage_source = df

        dosage_options = ["All"]
        if "Dosage Form" in dosage_source.columns:
            dosage_values = dosage_source["Dosage Form"].dropna().unique().tolist()
            dosage_options += sorted(dosage_values)

        dosage_filter = st.selectbox(
            "Dosage Form",
            dosage_options,
            key="dosage_filter"
        )

    # ---------------- APPLY FILTERS ----------------
    if salt_filter != "All":
        df = df[df["Salt + Strength"] == salt_filter]

    if dosage_filter != "All":
        df = df[df["Dosage Form"] == dosage_filter]

    return df