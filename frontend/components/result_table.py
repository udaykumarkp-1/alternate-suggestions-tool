import streamlit as st
import pandas as pd
import streamlit.components.v1 as components


def render_results_table(df: pd.DataFrame):

    if df.empty:
        st.warning("No results found.")
        return

    df = df.reset_index(drop=True)

    rows_html = ""

    for i, row in df.iterrows():

        salt = row.get("Salt + Strength", "")

        # split molecule + strength
        parts = salt.split(" ", 1)
        name = parts[0]
        strength = parts[1] if len(parts) > 1 else ""

        alt1 = "" if pd.isna(row.get("Alt 1")) else row.get("Alt 1")
        alt2 = "" if pd.isna(row.get("Alt 2")) else row.get("Alt 2")
        alt3 = "" if pd.isna(row.get("Alt 3")) else row.get("Alt 3")

        alt1_html = f'<span class="pill">• {alt1}</span>' if alt1 else '<span class="dash">—</span>'
        alt2_html = f'<span class="pill">• {alt2}</span>' if alt2 else '<span class="dash">—</span>'
        alt3_html = f'<span class="pill">• {alt3}</span>' if alt3 else '<span class="dash">—</span>'

        rows_html += f"""
        <tr>
            <td class="index">{i+1}</td>

            <td class="salt">
                <div class="salt-name">{name}</div>
                <div class="salt-strength">{strength}</div>
            </td>

            <td>{alt1_html}</td>
            <td>{alt2_html}</td>
            <td>{alt3_html}</td>
        </tr>
        """

    html = f"""
<style>

body {{
font-family: 'DM Sans', sans-serif;
}}

.table-wrap {{
background:white;
border-radius:12px;
border:1px solid #E2E8F4;
overflow:hidden;
}}

table {{
width:100%;
border-collapse:collapse;
font-size:14px;
}}

thead tr {{
background:#0D2137;
}}

thead th {{
padding:16px 20px;
text-align:left;
font-size:12px;
letter-spacing:0.08em;
color:#A8B8CC;
text-transform:uppercase;
}}

thead th:first-child {{
color:white;
}}

tbody tr {{
border-bottom:1px solid #E2E8F4;
}}

tbody tr:nth-child(even) {{
background:#F7F9FD;
}}

tbody tr:hover {{
background:#EEF4FF;
}}

tbody td {{
padding:18px 20px;
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
<th>ALTERNATIVE 1</th>
<th>ALTERNATIVE 2</th>
<th>ALTERNATIVE 3</th>
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
        height=520,
        scrolling=True
    )