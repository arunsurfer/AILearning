What is MCP?
 MCP ( Model Context Provider) is a tool for managing and providing context to AI models. 
 It allows users to define, store, and retrieve context information that can be used to enhance the performance of AI models in various applications.
 Consider it as a universal bridge between AI models and the context they need to operate effectively.


 Why MCP?

 Context Aware AI: MCP enables AI models to access relevant context, improving their accuracy and relevance in responses.
 Standard Communication: It provides a standardized way to manage context across different AI models and applications.
 Scalability: MCP can handle large volumes of context data, making it suitable for enterprise-level applications.
 Plug-in Architecture: MCP can be easily integrated with existing AI models and applications, allowing for seamless context management.


 MCP in .Net

 MCP is designed to be language-agnostic, but it has a strong focus on .Net applications.

 It provides a set of APIs and libraries that can be easily integrated into .Net applications, allowing developers to leverage the power of context-aware AI without having to build everything from scratch.

 Build MCP servers that explose tools(functions, APIs, services)
 Create MCP clients that can connect to these servers and use the provided tools
 Integrate with AI platforms like OpenAI, Azure AI, or custom AI models


 MCP Architecture

 Components:			Role of each component in the MCP architecture
 Host - AI powered app (copilot, chat, etc.)
 Client - MCP client that connects to the MCP server
 Server - Exposes tools and resources to the client


 Example Use Cases

 Imagine you are building a .Net app that lets AI
 * Fetch weather data from a third-party API
 * Summarize documents using an AI model
 * Run sql queries against a database

 you can use MCP to create a server that exposes these tools as APIs.
 1. Create a MCP server that defines the tools you need
 2. Register the server with the MCP registry [McpServerTool]
 3. Let AI clients invoke them via MCP messages like tools/call


