Langchain is a framework for building applications powered by language models. It provides a set of tools and abstractions to help developers create complex applications that can understand and generate human-like text.

Why use Langchain?
- **Modular Design**: Langchain is designed to be modular, allowing developers to mix and match components as needed.
- **Extensibility**: It supports custom components, enabling developers to extend its functionality to suit specific needs.'
- **Tool Integration**: Langchain can integrate with various tools and APIs, making it versatile for different applications.
- **Community and Ecosystem**: Langchain has a growing community and ecosystem, providing resources, examples, and support for developers.
- **Language Model Agnostic**: It can work with different language models, giving developers flexibility in choosing the best model for their application.


Components of Langchain:
- **Chains**: Sequences of calls to language models or other components, allowing for complex workflows.
- **Agents**: Components that can make decisions based on input and interact with language models and tools.
- **Memory**: Mechanisms to store and retrieve information across interactions, enabling context-aware applications.
- **Tools**: Interfaces to external APIs or services, allowing the application to perform actions beyond text generation.
- **Data Connectors**: Components that facilitate interaction with various data sources, such as databases or file systems.
- **vectors**: Representations of text or other data in a format suitable for machine learning and similarity search.


What can you do with Langchain?
- **Chatbots**: Build conversational agents that can understand and respond to user queries in natural language.
- **Question Answering Systems**: Create systems that can answer questions based on a given context or knowledge base.
- **Text Generation**: Generate human-like text for various applications, such as content creation or summarization.
- **Data Analysis**: Analyze and extract insights from text data using language models.
- **Search and Retrieval**: Implement search functionalities that leverage language models to understand user queries and retrieve relevant information.
- **Automation**: Automate tasks by integrating language models with external tools and APIs, enabling complex workflows.



![Intro](https://github.com/user-attachments/assets/3e08fa63-2d0b-4a64-b433-1f39a8ad35ef)


# LangChain AI Assistant

This project is a conversational agent built with LangChain, OpenAI, and ChromaDB. It supports memory, tool integration, and semantic retrieval.

## Features
- Conversational memory with ChromaDB
- Calculator tool integration
- Retrieval-augmented generation (RAG)
- Streamlit UI for interaction

## Setup
```bash
pip install langchain chromadb openai streamlit


