import streamlit as st

from services.nodes import get_unit_links

from ui.components import (
    header,
    bottom_navigation
)


def render():

    header()

    node_id = st.session_state.get(
        "node_id"
    )

    title = st.session_state.get(
        "node_title",
        "Resources"
    )

    st.markdown(
        f"## 📖 {title}"
    )

    if not node_id:

        st.warning(
            "No course unit selected."
        )

        bottom_navigation()

        return

    links = get_unit_links(
        node_id
    )

    if not links:

        st.info(
            "No resources are currently available."
        )

        bottom_navigation()

        return

    youtube = []
    notes = []
    questions = []

    for link in links:

        kind = link.get(
            "link_kind"
        )

        if kind == "youtube":

            youtube.append(link)

        elif kind == "drive_notes":

            notes.append(link)

        elif kind == "drive_questions":

            questions.append(link)

    render_links(
        "▶️ YouTube",
        youtube
    )

    render_links(
        "📄 Lecture Notes",
        notes
    )

    render_links(
        "❓ Questions",
        questions
    )

    bottom_navigation()


def render_links(
    heading,
    links
):

    st.markdown(
        f"### {heading}"
    )

    if not links:

        st.caption(
            "Nothing available."
        )

        return

    for link in links:

        with st.container(
            border=True
        ):

            st.markdown(
                f"**{link.get('title', 'Resource')}**"
            )

            if link.get("description"):

                st.caption(
                    link["description"]
                )

            if link.get("url"):

                st.link_button(
                    "Open Resource",
                    link["url"]
                )
