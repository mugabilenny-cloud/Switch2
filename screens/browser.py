import streamlit as st

from services.nodes import get_children

from ui.components import (
    header,
    bottom_navigation
)


def render():

    header()

    node_id = st.session_state.get(
        "node_id"
    )

    node_title = st.session_state.get(
        "node_title",
        "Browse"
    )

    st.markdown(
        f"## 📂 {node_title}"
    )

    if not node_id:

        st.warning(
            "No course section selected."
        )

        bottom_navigation()

        return

    children = get_children(
        node_id
    )

    if not children:

        st.info(
            "This section has no child folders."
        )

        if st.button(
            "📚 View Resources"
        ):

            st.session_state.page = "resource"

            st.rerun()

    else:

        for child in children:

            with st.container(
                border=True
            ):

                st.markdown(
                    f"### 📁 {child.get('title', '')}"
                )

                if child.get("node_type"):

                    st.caption(
                        child["node_type"]
                    )

                if st.button(
                    "Open",
                    key=f"child_{child['id']}"
                ):

                    st.session_state.node_id = (
                        child["id"]
                    )

                    st.session_state.node_title = (
                        child.get("title", "Browse")
                    )

                    st.rerun()

    bottom_navigation()
