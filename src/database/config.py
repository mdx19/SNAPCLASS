import streamlit as st
from supabase import create_client, Client, ClientOptions

supabase: Client = create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_KEY"],
    options=ClientOptions(postgrest_client_timeout=10)
)