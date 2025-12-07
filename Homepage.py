import streamlit as st
from langchain.chat_models import ChatOpenAI

# from langchain_core.prompts import ChatPromptTemplate
# from langchain_ollama.llms import OllamaLLM

# template = """Question: {question}

# Answer: Let's think step by step."""

# prompt = ChatPromptTemplate.from_template(template)

# model = OllamaLLM(model="llama3.1")

# chain = prompt | model

# chain.invoke({"question": "What is LangChain?"})

# Initialize the ChatOpenAI object
chat = None

if "OPENAI_API_KEY" not in st.session_state:
    st.session_state["OPENAI_API_KEY"] = ""
else:
    chat = ChatOpenAI(openai_api_key=st.session_state["OPENAI_API_KEY"], temperature=0)

if "PINECONE_API_KEY" not in st.session_state:
    st.session_state["PINECONE_API_KEY"] = ""

if "PINECONE_ENVIRONMENT" not in st.session_state:
    st.session_state["PINECONE_ENVIRONMENT"] = ""

st.set_page_config(page_title="Welcome to ASL", layout="wide", initial_sidebar_state="expanded")

st.title("Welcome to ASL")


with st.container():
    st.header("OpenAI Settings (ASL)")

    st.markdown(f"""
                | OpenAI API Key |
                |----------------|
                | {st.session_state["OPENAI_API_KEY"] if st.session_state["OPENAI_API_KEY"] else "Not Set"} |
                """)
    
with st.container():
    st.header("Pinecone Settings (ASL)")
    st.markdown(f"""
                | Pinecone API Key | Pinecone Environment |
                |------------------|----------------------|
                | {st.session_state["PINECONE_API_KEY"] if st.session_state["PINECONE_API_KEY"] else "Not Set"} | {st.session_state["PINECONE_ENVIRONMENT"] if st.session_state["PINECONE_ENVIRONMENT"] else "Not Set"} |
                """)
    
if chat:
    with st.container():
        st.header("OpenAI Chat Model Test")
        user_input = st.text_input("Enter a message to send to the OpenAI chat model:", key="chat_input")
        if st.button("Send", key="send_button"):
            if user_input:
                response = chat.agenerate([[user_input]])
                st.markdown(f"**Response:** {response.generations[0][0].text}")
            else:
                st.warning("Please enter a message before sending.")