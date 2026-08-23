import streamlit as st


def header():

    col1, col2 = st.columns(
        [5, 1]
    )

    with col1:

        st.markdown(
            "# 📚 Campus Notes"
        )

    with col2:

        if st.button("🔔"):

            st.session_state.page = (
                "notifications"
            )

            st.rerun()


def bottom_navigation():

    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        if st.button("🏠 Home"):

            st.session_state.page = "home"
            st.rerun()

    with col2:

        if st.button("📚 Courses"):

            st.session_state.page = "courses"
            st.rerun()

    with col3:

        if st.button("🔎 Search"):

            st.session_state.page = "search"
            st.rerun()

    with col4:

        if st.button("🔖 Saved"):

            st.session_state.page = "saved"
            st.rerun()
