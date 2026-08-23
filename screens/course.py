import streamlit as st

from services.nodes import get_root_nodes

from ui.components import (
    header,
    bottom_navigation
)


def render():

    header()

    st.markdown(
        "## 📚 My Courses"
    )

    st.caption(
        "Browse the academic content available to you."
    )

    nodes = get_root_nodes()

    for node in nodes:

        with st.container(
            border=True
        ):

            st.markdown(
                f"### {node.get('title', '')}"
            )

            if st.button(
                "Open",
                key=f"course_{node['id']}"
            ):

                st.session_state.node_id = (
                    node["id"]
                )

                st.session_state.node_title = (
                    node.get("title", "")
                )

                st.session_state.page = (
                    "browser"
                )

                st.rerun()

    bottom_navigation()
