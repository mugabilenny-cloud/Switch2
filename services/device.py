import streamlit as st
import uuid

from services.supabase import get_supabase


def get_device_token():

    if "device_token" not in st.session_state:

        st.session_state.device_token = str(
            uuid.uuid4()
        )

    return st.session_state.device_token


def get_home_node():

    return st.session_state.get(
        "home_node_id"
    )


def set_home_node(node_id):

    st.session_state.home_node_id = node_id


def register_device():

    supabase = get_supabase()

    device_token = get_device_token()

    home_node_id = get_home_node()

    result = supabase.rpc(
        "fn_register_device",
        {
            "p_device_token": device_token,
            "p_home_node_id": home_node_id
        }
    ).execute()

    return result.data
