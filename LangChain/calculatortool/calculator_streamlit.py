import os
import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.memory import VectorStoreRetrieverMemory
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.agents import initialize_agent, AgentType

# === Page config ===
st.set_page_config(page_title="LangChain Assistant", layout="wide")
st.title("🤖 LangChain AI Assistant with Memory")

# === Load API Key ===
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# === Cache agent creation to avoid reloading ===
@st.cache_resource
def create_agent():
    embedding = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    vector_store = Chroma(collection_name="memory_store", embedding_function=embedding)

    memory = VectorStoreRetrieverMemory(
        retriever=vector_store.as_retriever(search_kwargs={"k": 5}),
        memory_key="chat_history"
    )

    llm = ChatOpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)

    return initialize_agent(
        tools=[],  # Add tools like calculator or search here
        llm=llm,
        agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
        memory=memory,
        verbose=True
    )

agent = create_agent()

# === Session State for Chat ===
if "history" not in st.session_state:
    st.session_state.history = []

# === Chat Input Form ===
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("🗨️ You:", "")
    submitted = st.form_submit_button("Send")

if submitted and user_input:
    try:
        response = agent.run(user_input)
    except Exception as e:
        response = f"⚠️ Error: {str(e)}"
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Assistant", response))

# === Display Chat History ===
for speaker, message in st.session_state.history:
    st.markdown(f"**{speaker}:** {message}")

# === Reset Button ===
if st.button("🧹 Clear Chat"):
    st.session_state.history = []