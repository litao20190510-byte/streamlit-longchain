import streamlit as st

if "OPENAI_API_KEY" not in st.session_state:
    st.session_state["OPENAI_API_KEY"] = ""

st.set_page_config(
    page_title="OpenAI Settings", layout="wide", initial_sidebar_state="expanded")


st.title("OpenAI Settings")

openai_api_key = st.text_input("OpenAI API Key", value=st.session_state["OPENAI_API_KEY"], max_chars=None, key=None, type="password")

saved = st.button("Save Settings")

if saved:
    st.session_state["OPENAI_API_KEY"] = openai_api_key
    st.success("Settings saved successfully!")