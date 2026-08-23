import streamlit as st

from services.nodes import get_root_nodes
from services.ads import get_ads

from ui.components import (
    header,
    bottom_navigation
)


def render():

    header()

    st.markdown(
        "### Find your course material"
    )

    query = st.text_input(
        "Search",
        placeholder="Search PHA 2101, Biochemistry, notes...",
        label_visibility="collapsed"
    )

    if query:

        st.session_state.search_query = query

        st.session_state.page = "search"

        st.rerun()

    st.markdown(
        "### 🎓 Universities"
    )

    nodes = get_root_nodes()

    if not nodes:

        st.info(
            "No university nodes are available yet."
        )

    for node in nodes:

        with st.container(border=True):

            st.markdown(
                f"### {node.get('title', 'Untitled')}"
            )

            if st.button(
                "Open",
                key=f"root_{node['id']}"
            ):

                st.session_state.node_id = node["id"]

                st.session_state.node_title = (
                    node.get("title", "Browse")
                )

                st.session_state.page = "browser"

                st.rerun()

    st.markdown(
        "### 📢 For you"
    )

    ads = get_ads()

    for ad in ads:

        with st.container(border=True):

            st.markdown(
                f"**{ad.get('title', '')}**"
            )

            if ad.get("headline"):

                st.write(
                    ad["headline"]
                )

            if ad.get("body"):

                st.caption(
                    ad["body"]
                )

            if ad.get("cta_label"):

                st.link_button(
                    ad["cta_label"],
                    ad["cta_url"]
                )

    bottom_navigation()
