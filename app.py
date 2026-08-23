import streamlit as st

from services.device import register_device

from screens import home
from screens import search
from screens import courses
from screens import browser
from screens import resource
from screens import saved
from screens import notifications
from screens import onboarding


st.set_page_config(
    page_title="Campus Notes",
    page_icon="📚",
    layout="centered"
)


if "page" not in st.session_state:

    st.session_state.page = "home"


if "device_registered" not in st.session_state:

    try:

        register_device()

        st.session_state.device_registered = True

    except Exception as error:

        st.session_state.device_registered = False

        st.error(
            "Could not connect to Supabase."
        )

        st.exception(error)


pages = {

    "home": home.render,

    "search": search.render,

    "courses": courses.render,

    "browser": browser.render,

    "resource": resource.render,

    "saved": saved.render,

    "notifications": notifications.render,

    "onboarding": onboarding.render
}


current_page = st.session_state.page

pages.get(
    current_page,
    home.render
)()
