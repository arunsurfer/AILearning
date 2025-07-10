from langchain.agents import Tool, initialize_agent, AgentType
from langchain.llms import OpenAI
import os
from dotenv import load_dotenv
from langchain.tools import StructuredTool
from pydantic import BaseModel


# Load environment variables from .env file or take it from system environment

openai_api_key = os.getenv("OPENAI_API_KEY")


# Define calculator tool

# Define input schema
class CalculatorInput(BaseModel):
    expression: str


def calculator_tool(expression: str) -> str:
    try:
        # Evaluate the expression safely
        result = eval(expression, {"__builtins__": None}, {})
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"
    
# Initialize the calculator tool    
calculator = Tool(
    name="Calculator",
    func=calculator_tool,
    description="A tool to perform basic arithmetic calculations. Input should be a valid Python expression."
)

# Initialize the agent with the calculator tool
llm = OpenAI(temperature=0)
agent = initialize_agent(
    tools=[calculator],
    llm=llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
     handle_parsing_errors=True, 
    verbose=True
)

# Example usage of the agent
response = agent.run("What is the result of 3 + 5 * (2 - 1)?")
print(response)  # Should print the result of the calculation