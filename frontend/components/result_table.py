import streamlit as st
import pandas as pd
import streamlit.components.v1 as components


def render_results_table(df: pd.DataFrame):

    if df.empty:
        st.warning("No results found.")
        return

    # Reset index so row numbers start from 1 on each page
    df = df.reset_index(drop=True)

    rows_html = ""

    for i, row in df.iterrows():

        salt = row.get("Salt + Strength", "")

        alt1 = "" if pd.isna(row.get("Alt 1")) else row.get("Alt 1")
        alt2 = "" if pd.isna(row.get("Alt 2")) else row.get("Alt 2")
        alt3 = "" if pd.isna(row.get("Alt 3")) else row.get("Alt 3")

        alt1_html = f'<span class="alt-pill">{alt1}</span>' if alt1 else '<span class="empty-alt">—</span>'
        alt2_html = f'<span class="alt-pill">{alt2}</span>' if alt2 else '<span class="empty-alt">—</span>'
        alt3_html = f'<span class="alt-pill">{alt3}</span>' if alt3 else '<span class="empty-alt">—</span>'

        rows_html += f"""
        <tr>
            <td class="row-index">{i+1}</td>
            <td><div class="salt-name">{salt}</div></td>
            <td>{alt1_html}</td>
            <td>{alt2_html}</td>
            <td>{alt3_html}</td>
        </tr>
        """

    table_html = f"""
    <div class="table-wrap">
        <table>
            <thead>
                <tr>
                    <th class="row-index">#</th>
                    <th>Salt + Strength</th>
                    <th>Alternative 1</th>
                    <th>Alternative 2</th>
                    <th>Alternative 3</th>
                </tr>
            </thead>
            <tbody>
                {rows_html}
            </tbody>
        </table>
    </div>
    """

    # Render HTML without Streamlit escaping it
    components.html(
        table_html,
        height=450,
        scrolling=True
    )