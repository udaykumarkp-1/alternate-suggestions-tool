import pandas as pd
import streamlit as st
from io import BytesIO
from services.processor import process_mapping


def upload_section():

    st.markdown("### 📤 Upload File")
    st.markdown(
        "<div style='color:#2563EB; font-weight:500; margin-bottom:15px;'>Upload CSV / Excel → Get Alternate Suggestions</div>",
        unsafe_allow_html=True
    )

    uploaded_file = st.file_uploader("", type=["xlsx"])

    if uploaded_file:
        with st.spinner("Processing file... Please wait..."):
            try:
                # 🔥 Call new processor logic
                output_file, max_alts = process_mapping(uploaded_file)

                st.success("🎉 Alternate suggestions generated successfully!")

                st.download_button(
                    "📥 Download Processed File",
                    data=output_file,
                    file_name="Mapped_Output.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )

            except Exception as e:
                st.error(str(e))