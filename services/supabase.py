import streamlit as st
from supabase import create_client


@st.cache_resource
def get_supabase():

    url = st.secrets["SUPABASE_URL"]

    anon_key = st.secrets["SUPABASE_ANON_KEY"]

    return create_client(
        url,
        anon_key
    )
