import streamlit as st
from services.api import check_data_status


def render_history_page():

    st.markdown("### System History & Status")

    st.markdown(
        """
        This page shows information about stored mappings and system usage.
        Uploaded mappings are permanently stored in the database and become searchable.
        """
    )

    st.markdown("---")

    # ---------------- DATABASE STATUS ----------------

    st.markdown("#### Database Status")

    try:
        status = check_data_status()

        if status.get("has_data"):

            st.success("Database contains stored mappings.")

        else:

            st.warning("No data found in database yet.")

    except Exception as e:

        st.error(f"Could not connect to backend: {str(e)}")

    st.markdown("---")

    # ---------------- PLACEHOLDER SECTIONS ----------------

    st.markdown("#### Recent Uploads")

    st.info(
        "Upload history will appear here in future versions."
    )

    st.markdown("#### Recent Searches")

    st.info(
        "Search analytics will appear here in future versions."
    )