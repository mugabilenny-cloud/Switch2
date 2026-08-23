import streamlit as st

from ui.components import (
    header,
    bottom_navigation
)


def render():

    header()

    st.markdown(
        "## 🔖 Saved"
    )

    st.info(
        "Saved resources are not yet supported "
        "by the current database schema."
    )

    st.caption(
        "This screen is reserved for a future "
        "bookmark/offline feature."
    )

    bottom_navigation()
