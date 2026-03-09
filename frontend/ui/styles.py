import streamlit as st


def load_styles():

    st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@500;600;700&family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">

    <style>

    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
    }

    .stApp {
        background:#F0F4FA;
    }

    /* REMOVE TOP SPACE */

    .block-container{
    padding-top:3rem;
    padding-bottom:1rem;
    max-width:1400px;
    }

    #MainMenu {visibility:hidden;}
    footer {visibility:hidden;}
    

    /* HERO TEXT */

    .hero-title{
        font-family:'Bricolage Grotesque', sans-serif;
        font-size:24px;
        font-weight:700;
        color:#0D2137;
        margin-bottom:4px;
    }

    .hero-sub{
        font-size:13px;
        color:#6B82A0;
        margin-bottom:18px;
    }

    /* SEARCH INPUT */

    .search-input input{
        height:48px;
        border-radius:11px;
        border:1.5px solid #E2E8F4;
        padding-left:12px;
        font-size:14px;
    }

    /* TABLE */

    .table-wrap{
        background:white;
        border-radius:14px;
        border:1px solid #E2E8F4;
        overflow:hidden;
        box-shadow:0 2px 16px rgba(13,33,55,0.06);
        max-height:420px;
        overflow-y:auto;
        margin-top:15px;
    }

    table{
        width:100%;
        border-collapse:collapse;
        font-size:13.5px;
    }

    thead{
        position:sticky;
        top:0;
        z-index:10;
    }

    thead tr{
        background:#0D2137;
    }

    thead th{
        padding:13px 18px;
        text-align:left;
        font-size:11px;
        letter-spacing:0.08em;
        color:rgba(255,255,255,0.9);
        text-transform:uppercase;
    }

    tbody tr{
        border-bottom:1px solid #E2E8F4;
    }

    tbody tr:hover{
        background:#F6F9FF;
    }

    tbody td{
        padding:13px 18px;
    }

    .row-index{
        width:40px;
        text-align:center;
        color:#6B82A0;
    }

    .salt-name{
        font-weight:600;
        color:#0D2137;
        font-size:13px;
    }

    .alt-pill{
        background:#EBF7F4;
        color:#0A6E56;
        font-size:12px;
        padding:4px 10px;
        border-radius:6px;
        display:inline-block;
    }

    .empty-alt{
        color:#C8D4E0;
        font-style:italic;
    }

    </style>
    """, unsafe_allow_html=True)