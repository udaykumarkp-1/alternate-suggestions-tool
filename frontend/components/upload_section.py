import pandas as pd
import streamlit as st
from io import BytesIO
from services.processor import process_mapping
from services.api import save_payload


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
                # Process file
                output_file, max_alts = process_mapping(uploaded_file)

                # 🔥 IMPORTANT PART — SAVE TO BACKEND

                # Read processed file again as dataframe
                output_file.seek(0)
                final_df = pd.read_excel(output_file)

                # Replace NaN with empty string
                final_df = final_df.fillna("")

                # Convert to JSON records
                payload = final_df.to_dict(orient="records")

                # Send to backend
                res = save_payload(payload)

                if res.status_code == 200:
                    st.success("🎉 Alternate suggestions generated and saved successfully!")
                else:
                    st.error("Failed to save data to backend")

                # Download button
                output_file.seek(0)
                st.download_button(
                    "📥 Download Processed File",
                    data=output_file,
                    file_name="Mapped_Output.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )

            except Exception as e:
                st.error(str(e))