import streamlit as st
import pandas as pd
import streamlit.components.v1 as components


def render_results_table(df: pd.DataFrame):

    if df.empty:
        st.warning("No results found.")
        return

    # Keep Dosage Form for display, remove only from alt logic
    display_df = df.copy()
    if "Dosage Form" in display_df.columns:
        display_df = display_df.drop(columns=["Dosage Form"])

    display_df = display_df.reset_index(drop=True)

    # Detect all Alt columns dynamically
    alt_columns = [col for col in display_df.columns if col.startswith("Alt ")]

    # Build table headers
    alt_headers = ""
    for col in alt_columns:
        alt_headers += f'<th>{col.upper()}</th>\n'

    rows_html = ""

    for i, row in display_df.iterrows():

        salt = row.get("Salt + Strength", "")
        parts = salt.split(" ", 1)
        name = parts[0]
        strength = parts[1] if len(parts) > 1 else ""

        alt_cells = ""
        for col in alt_columns:
            val = row.get(col, "")
            if pd.isna(val) or val == "":
                alt_cells += '<td><span class="dash">—</span></td>\n'
            else:
                alt_cells += f'<td><span class="pill">• {val}</span></td>\n'

        rows_html += f"""
        <tr>
            <td class="index">{i+1}</td>
            <td class="salt">
                <div class="salt-name">{name}</div>
                <div class="salt-strength">{strength}</div>
            </td>
            {alt_cells}
        </tr>
        """

    # Estimate height based on rows
    table_height = max(300, min(600, 60 + len(display_df) * 58))

    html = f"""
<style>
body {{ font-family: 'DM Sans', sans-serif; }}

.table-wrap {{
background:white;
border-radius:12px;
border:1px solid #E2E8F4;
overflow:auto;
}}

table {{
width:100%;
border-collapse:collapse;
font-size:14px;
min-width:700px;
}}

thead tr {{ background:#0D2137; }}

thead th {{
padding:16px 20px;
text-align:left;
font-size:12px;
letter-spacing:0.08em;
color:rgba(255,255,255,0.9);
text-transform:uppercase;
white-space:nowrap;
}}

tbody tr {{ border-bottom:1px solid #E2E8F4; }}
tbody tr:nth-child(even) {{ background:#F7F9FD; }}
tbody tr:hover {{ background:#EEF4FF; }}

tbody td {{
padding:14px 20px;
vertical-align:middle;
}}

.index {{
width:40px;
text-align:center;
color:#6B82A0;
font-weight:500;
}}

.salt-name {{
font-weight:700;
color:#0D2137;
font-size:14px;
}}

.salt-strength {{
font-size:12px;
color:#6B82A0;
margin-top:2px;
}}

.pill {{
background:#E6F6F2;
color:#087F67;
font-size:13px;
padding:6px 12px;
border-radius:8px;
display:inline-block;
white-space:nowrap;
}}

.dash {{
color:#C8D4E0;
font-style:italic;
}}
</style>

<div class="table-wrap">
<table>
<thead>
<tr>
<th>#</th>
<th>SALT + STRENGTH</th>
{alt_headers}
</tr>
</thead>
<tbody>
{rows_html}
</tbody>
</table>
</div>
"""

    components.html(
        html,
        height=table_height,
        scrolling=True
    )