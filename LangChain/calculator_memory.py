# === Load environment variables ===
import os
from dotenv import load_dotenv

# === LangChain core components ===
from langchain.chat_models import ChatOpenAI
from langchain.memory import VectorStoreRetrieverMemory
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.agents import initialize_agent, AgentType


# === Step 1: Load your OpenAI API key from .env file ===
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# === Step 2: Create an embedding model ===
# This model converts text into vector form for similarity search
embedding = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)


# === Step 3: Set up ChromaDB vector store ===
# Chroma stores conversation chunks as embeddings
vector_store = Chroma(
    collection_name="memory_store",
    embedding_function=embedding
)

# === Step 4: Define memory using vector store ===
# Retrieves top 5 similar messages when responding
memory = VectorStoreRetrieverMemory(
    retriever=vector_store.as_retriever(search_kwargs={"k": 5}),
    memory_key="chat_history"
)

# === Step 5: Initialize the language model (LLM) ===
# Using ChatOpenAI with temperature 0 for focused answers
llm = ChatOpenAI(
    temperature=0,
    openai_api_key=OPENAI_API_KEY
)

# === Step 6: Build the conversational agent ===
# Can support reasoning and tool integration
agent = initialize_agent(
    tools=[],  # You can add tools like calculator/search here
    llm=llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=True  # Shows reasoning steps during execution
)

# === Step 7: Create a live conversation loop ===
print("LangChain AI Assistant is ready! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    # Run the agent and display the response
    response = agent.run(user_input)
    print(f"Assistant: {response}")