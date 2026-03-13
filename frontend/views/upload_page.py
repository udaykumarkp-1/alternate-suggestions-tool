import streamlit as st
import pandas as pd

from services.processor import process_mapping
from services.api import save_payload


def render_upload_page():

    st.markdown("### Bulk Upload")

    st.markdown(
        """
        Upload a CSV or Excel file to process multiple products at once.
        The processed results will be stored in the database and become searchable.
        """
    )

    uploaded_file = st.file_uploader(
        "Upload file",
        type=["xlsx", "csv"]
    )

    if uploaded_file is None:
        return

    # ---------------- PROCESS FILE ----------------

    with st.spinner("Processing file..."):

        try:
            output_file, processed_df = process_mapping(uploaded_file)

        except Exception as e:
            st.error(f"Processing failed: {str(e)}")
            return

    st.success("File processed successfully.")

    # ---------------- REMOVE UNWANTED COLUMN ----------------

    # Sometimes processor or Excel may introduce a 'Dosage' column
    # We remove it safely if present
    processed_df = processed_df.drop(columns=["Dosage"], errors="ignore")

    # ---------------- PREVIEW ----------------

    st.markdown("### Preview Processed Data")

    st.dataframe(
        processed_df,
        use_container_width=True
    )

    # ---------------- SAVE TO DATABASE ----------------

    payload = processed_df.to_dict(orient="records")

    try:
        save_payload(payload)
        st.success("Data stored in database successfully.")
    except Exception as e:
        st.error(f"Failed to save data: {str(e)}")

    # ---------------- DOWNLOAD OUTPUT ----------------

    st.download_button(
        label="Download Processed File",
        data=output_file,
        file_name="processed_mapping.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )