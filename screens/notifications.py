import streamlit as st

from services.notifications import (
    get_notifications,
    mark_seen
)

from ui.components import (
    header,
    bottom_navigation
)


def render():

    header()

    st.markdown(
        "## 🔔 Notifications"
    )

    notifications = get_notifications()

    if not notifications:

        st.info(
            "No new notifications."
        )

        bottom_navigation()

        return

    for notification in notifications:

        notification_id = notification[
            "notification_id"
        ]

        with st.container(
            border=True
        ):

            st.markdown(
                f"### {notification.get('title', '')}"
            )

            st.write(
                notification.get(
                    "body",
                    ""
                )
            )

            if st.button(
                "Dismiss",
                key=f"dismiss_{notification_id}"
            ):

                mark_seen(
                    notification_id,
                    dismissed=True
                )

                st.rerun()

            else:

                # Notification has been shown.
                try:

                    mark_seen(
                        notification_id,
                        dismissed=False
                    )

                except Exception:
                    pass

    bottom_navigation()
