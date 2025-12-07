import streamlit as st

if "PINECONE_API_KEY" not in st.session_state:
    st.session_state["PINECONE_API_KEY"] = ""

if "PINECONE_ENVIRONMENT" not in st.session_state:
    st.session_state["PINECONE_ENVIRONMENT"] = ""

st.set_page_config(
    page_title="Pinecone Settings", layout="wide", initial_sidebar_state="expanded")

st.title("Pinecone Settings")

pinecone_api_key = st.text_input("Pinecone API Key", value=st.session_state["PINECONE_API_KEY"], max_chars=None, key=None, type="default")
pinecone_environment = st.text_input("Pinecone Environment", value=st.session_state["PINECONE_ENVIRONMENT"], max_chars=None, key=None, type="default")

saved = st.button("Save Settings")
if saved:
    st.session_state["PINECONE_API_KEY"] = pinecone_api_key
    st.session_state["PINECONE_ENVIRONMENT"] = pinecone_environment
    st.success("Settings saved successfully!")