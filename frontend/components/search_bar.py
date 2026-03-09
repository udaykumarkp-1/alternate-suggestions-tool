import streamlit as st


def render_search_bar():

    st.markdown(
        '<div class="hero-title">Search Alternate Products</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="hero-sub">Enter a salt name or product to find available alternatives</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([5,1])

    with col1:
        query = st.text_input(
            "",
            placeholder="e.g. Paracetamol 500mg, Metformin 1g…",
            label_visibility="collapsed",
            key="search_query"
        )

    with col2:
        search_clicked = st.button(
            "Search",
            use_container_width=True
        )

    # ENTER key also triggers search
    run_search = False

    if search_clicked:
        run_search = True

    if query and st.session_state.get("search_query"):
        run_search = True

    return query, run_search