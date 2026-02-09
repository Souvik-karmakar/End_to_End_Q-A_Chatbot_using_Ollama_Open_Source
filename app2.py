import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Ollama Q&A Chatbot",
    page_icon="🦙",
    layout="centered"
)

st.title("🦙 Ollama Q&A Chatbot")
st.caption("Open-source LLMs powered locally via Ollama")

# ---------------- PROMPT ----------------
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful and concise assistant."),
        ("user", "{question}")
    ]
)

def generate_response(question, model, temperature, max_tokens):
    llm = Ollama(
        model=model,
        temperature=temperature,
    )
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"question": question})

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.header("⚙️ Settings")

    model = st.selectbox(
        "Select Open-Source Model",
        ["phi3", "gemma2"]
    )

    temperature = st.slider(
        "Creativity (Temperature)",
        0.0, 1.0, 0.7
    )

    max_tokens = st.slider(
        "Max Tokens",
        50, 500, 200
    )

    st.divider()

    if st.button("🧹 Clear Chat"):
        st.session_state.messages = []

    st.caption("⚠️ Make sure Ollama is running locally")

# ---------------- SESSION STATE ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- CHAT HISTORY ----------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------- CHAT INPUT ----------------
user_prompt = st.chat_input("Ask something...")

if user_prompt:
    # User message
    st.session_state.messages.append(
        {"role": "user", "content": user_prompt}
    )
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking... 🤔"):
            try:
                response = generate_response(
                    user_prompt,
                    model,
                    temperature,
                    max_tokens
                )
                st.markdown(response)
                st.session_state.messages.append(
                    {"role": "assistant", "content": response}
                )
            except Exception as e:
                st.error(f"❌ Error: {e}")
