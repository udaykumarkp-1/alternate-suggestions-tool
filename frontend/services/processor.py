import pandas as pd
from io import BytesIO


def process_mapping(uploaded_file):

    if not uploaded_file.name.endswith(".xlsx"):
        raise Exception("Please upload only .xlsx file")

    # Read Excel sheets
    ufm_df = pd.read_excel(uploaded_file, sheet_name="Salt + Strength List")
    salt_df = pd.read_excel(uploaded_file, sheet_name="Salt + Strength(Mapped List)")

    # Clean column names
    ufm_df.columns = ufm_df.columns.str.strip()
    salt_df.columns = salt_df.columns.str.strip()

    # Required columns
    required_columns_ufm = ["Salt + Strength", "Item Name", "Qty sold", "TYPE"]
    required_columns_salt = ["Salt + Strength"]

    for col in required_columns_ufm:
        if col not in ufm_df.columns:
            raise Exception(f"Missing column in 'Salt + Strength List': {col}")

    for col in required_columns_salt:
        if col not in salt_df.columns:
            raise Exception(f"Missing column in 'Salt + Strength(Mapped List)': {col}")

    # ---------------- PRIORITY LOGIC ----------------
    priority = {
        "UFM": 1,
        "SFM": 2,
        "FM": 3,
        "Slow_Moving": 4
    }

    ufm_df["priority"] = ufm_df["TYPE"].map(priority)

    def get_all_items(group):
        group = group.sort_values(
            by=["priority", "Qty sold"],
            ascending=[True, False]
        )
        return group["Item Name"].drop_duplicates().tolist()

    grouped_items = (
        ufm_df.groupby("Salt + Strength")
        .apply(get_all_items)
        .reset_index(name="AllItems")
    )

    max_alts = grouped_items["AllItems"].apply(len).max()

    for i in range(max_alts):
        grouped_items[f"Alt {i+1}"] = grouped_items["AllItems"].apply(
            lambda x: x[i] if i < len(x) else ""
        )

    grouped_items = grouped_items.drop(columns=["AllItems"])

    final_df = salt_df.merge(
        grouped_items,
        on="Salt + Strength",
        how="left"
    )

    # Save to memory instead of disk
    output = BytesIO()
    final_df.to_excel(output, index=False)
    output.seek(0)

    return output, max_alts