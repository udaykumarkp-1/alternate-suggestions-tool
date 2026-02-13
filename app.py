import streamlit as st
import pandas as pd
from io import BytesIO

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Alternate Suggestions Tool",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>

/* FORCE LIGHT MODE EVEN IN DARK SYSTEM */
:root {
    color-scheme: light;
}

/* GLOBAL RESET */
html, body, [class*="css"] {
    background: #e9fbf8 !important;
    color: #111827 !important;
    font-family: "Segoe UI", sans-serif;
}

/* APP BACKGROUND */
.stApp {
    background: linear-gradient(135deg,#e9fbf8 0%,#f5fffd 100%) !important;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: #e6faf6 !important;
    border-right: 1px solid #d1f0ea;
}

/* SIDEBAR TEXT */
section[data-testid="stSidebar"] * {
    color: #111827 !important;
}

/* MAIN CARD */
.main > div {
    background: white !important;
    padding: 2rem;
    border-radius: 18px;
    box-shadow: 0 8px 30px rgba(0,0,0,.05);
}

/* HEADINGS */
h1, h2, h3 {
    color: #111827 !important;
}

/* FILE UPLOADER */
div[data-testid="stFileUploader"] {
    background: white !important;
    border: 2px dashed #18A999 !important;
    border-radius: 14px;
    padding: 20px;
}

/* BUTTONS */
button {
    background: #18A999 !important;
    color: white !important;
    border-radius: 10px !important;
}

/* SUCCESS BOX */
div[data-testid="stAlert"] {
    border-left: 6px solid #18A999;
    background: #f0fffb !important;
    color:#111827 !important;
}

/* INPUTS */
input, textarea {
    background:white !important;
    color:#111827 !important;
}

/* REMOVE STREAMLIT FOOTER */
footer {
    visibility:hidden;
}

/* REMOVE DARK MODE FILTERS */
[data-testid="stAppViewContainer"] {
    filter:none !important;
}

</style>
""", unsafe_allow_html=True)




# ---------------- SIDEBAR ----------------
st.sidebar.image("https://www.mrmed.in/nav/nav_logo.svg", width=250)
st.sidebar.title("Alternate Suggestions Tool")
st.sidebar.caption("Automated UFM Mapping Engine")

with st.sidebar.expander("📘 Instructions", expanded=True):
    st.markdown("""
### Supported Files

✔ Excel (.xlsx)  
✔ CSV (.csv)

---

### Sheet Format

#### Sheet 1: `new UFM List`
Required Columns:
- Salt + Strength  
- Item Name  
- Qty sold  

#### Sheet 2: `New UFM List(Mapped List)`
Required Columns:
- Salt + Strength  
                
(Column name must be exactly same)             
""")

# ---------------- MAIN PAGE ----------------
st.title("Alternate Suggestions Tool")
st.caption("Upload CSV / Excel → Get Alternate Suggestions")

st.markdown("### 📤 Upload File")
uploaded_file = st.file_uploader("", type=["xlsx", "csv"])

required_columns_ufm = ["Salt + Strength", "Item Name", "Qty sold"]
required_columns_salt = ["Salt + Strength"]

# ---------------- PROCESSING ----------------
if uploaded_file:
    with st.spinner("Processing file... Please wait..."):
        try:
            file_name = uploaded_file.name.lower()

            # CSV handling
            if file_name.endswith(".csv"):
                ufm_df = pd.read_csv(uploaded_file)
                salt_df = ufm_df.copy()

            # Excel handling
            else:
                ufm_df = pd.read_excel(uploaded_file, sheet_name="new UFM List")
                salt_df = pd.read_excel(uploaded_file, sheet_name="New UFM List(Mapped List)")

            ufm_df.columns = ufm_df.columns.str.strip()
            salt_df.columns = salt_df.columns.str.strip()

            if not all(col in ufm_df.columns for col in required_columns_ufm):
                st.error("❌ Missing required columns in input file")
                st.stop()

            if not all(col in salt_df.columns for col in required_columns_salt):
                st.error("❌ Missing 'Salt + Strength' column")
                st.stop()

            ufm_df = ufm_df.sort_values(by="Qty sold", ascending=False)

            top_items = (
                ufm_df.groupby("Salt + Strength")
                .apply(lambda x: x["Item Name"].head(3).tolist())
                .reset_index(name="TopItems")
            )

            top_items["Alt 1 (UFM/SFM/FM)"] = top_items["TopItems"].apply(lambda x: x[0] if len(x)>0 else "")
            top_items["Alt 2 (UFM/SFM/FM)"] = top_items["TopItems"].apply(lambda x: x[1] if len(x)>1 else "")
            top_items["Alt 3 (UFM/SFM/FM)"] = top_items["TopItems"].apply(lambda x: x[2] if len(x)>2 else "")

            top_items = top_items.drop(columns=["TopItems"])

            final_df = salt_df.merge(top_items, on="Salt + Strength", how="left")

            output = BytesIO()

            # Output format based on input
            if file_name.endswith(".csv"):
                final_df.to_csv(output, index=False)
                mime = "text/csv"
                output_name = uploaded_file.name

            else:
                with pd.ExcelWriter(output, engine="openpyxl") as writer:
                    final_df.to_excel(writer, sheet_name="New UFM List(Mapped List)", index=False)
                mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                output_name = uploaded_file.name

            st.success("🎉 Alternate suggestions generated successfully!")

            st.download_button(
                "📥 Download Processed File",
                data=output.getvalue(),
                file_name=output_name,
                mime=mime
            )

        except Exception as e:
            st.error(str(e))

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    "<p style='text-align:center;font-size:12px;'>Alternate Suggestions Tool | Version 1.1 (Built by Uday)</p>",
    unsafe_allow_html=True
)




