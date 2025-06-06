# main.py
from langchain.agents import initialize_agent, Tool
from langchain_community.llms import Ollama
from file_tools import list_files, classify_and_move

llm = Ollama(model="llama3")

tools = [
    Tool(
        name="FileOrganizer",
        func=classify_and_move,
        description="Organizes files into folders based on their names and types."
    )
]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)

# Ask agent to organize
directory = "sample_files"
agent.run(f"Organize the files in the '{directory}' directory based on their type and content.")
