import streamlit as st

from services.search import search_tree

from ui.components import (
    header,
    bottom_navigation
)


def render():

    header()

    st.markdown(
        "## 🔎 Search"
    )

    query = st.text_input(
        "Search the repository",
        value=st.session_state.get(
            "search_query",
            ""
        ),
        placeholder="PHA 2101, pharmacology..."
    )

    if not query:

        st.caption(
            "Search courses, topics and resources."
        )

        bottom_navigation()

        return

    results = search_tree(
        query
    )

    if not results:

        st.info(
            "No results found."
        )

        bottom_navigation()

        return

    for index, result in enumerate(
        results
    ):

        result_type = result.get(
            "result_type"
        )

        title = result.get(
            "title",
            "Untitled"
        )

        node_path = result.get(
            "node_path",
            ""
        )

        with st.container(
            border=True
        ):

            if result_type == "node":

                st.markdown(
                    f"📁 **{title}**"
                )

            else:

                st.markdown(
                    f"🔗 **{title}**"
                )

            st.caption(
                node_path
            )

            if st.button(
                "Open",
                key=f"search_result_{index}"
            ):

                st.session_state.node_id = (
                    result["id"]
                )

                st.session_state.node_title = (
                    title
                )

                if result_type == "node":

                    st.session_state.page = (
                        "browser"
                    )

                else:

                    st.session_state.page = (
                        "resource"
                    )

                st.rerun()

    bottom_navigation()
