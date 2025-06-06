# 🤖 Smart File Organizer Agent (Generative AI Project)

This is a local AI-powered tool that **organizes files automatically** based on their name, type, and basic content. It uses a **Generative AI agent** powered by LangChain and Ollama to simulate intelligent reasoning for file management.

---

## 🚀 Features

- ✅ Uses local LLM (e.g., LLaMA3) via Ollama
- 📂 Organizes files into folders (resumes, invoices, images, PDFs)
- 🧠 Powered by LangChain agent + custom tool
- ⚙️ Built entirely in Python — runs locally, no cloud required
- 💬 Agent-style interactions with decision-making logic

---

## 🛠️ Tech Stack

| Tool              | Purpose                         |
|-------------------|----------------------------------|
| [Ollama](https://ollama.com)           | Run local LLM models like LLaMA3 |
| [LangChain](https://www.langchain.com) | Create agent and tool interface  |
| Python            | File system logic               |

---

## 📁 Project Structure
├── main.py # Entry point for the agent
├── file_tools.py # File classification & moving logic
├── sample_files/ # Folder with unorganized files
├── organized_files/ # Output folder with categorized files
└── README.md 

## ⚙️ Installation & Setup

1. **Clone the repo**
```bash
git clone https://github.com/yourusername/smart-file-organizer.git
cd smart-file-organizer

2. Set up Python environment
python -m venv fileagent-env
.\fileagent-env\Scripts\activate  # Windows
# OR
source fileagent-env/bin/activate  # Linux/Mac

pip install langchain langchain-community ollama python-dotenv

3. Install Ollama and run a model
    Download Ollama and install ollama
    https://ollama.com/download/linux
    
    Pull and run the model:
    ollama run llama3


▶️ Usage
1. Place files to organize in the sample_files/ folder: 
resume_john.pdf
invoice_123.pdf
photo.png
notes.pdf

2. Run the script:
python main.py

3. Files will be automatically moved to organized folders inside organized_files/:
organized_files/
├── Resumes/
├── Invoices/
├── Images/
├── PDFs/
├── Others/

🔍 How It Works
LangChain creates an agent with a tool: FileOrganizer

The tool runs custom logic to classify and move files based on:

Filename keywords (like "resume", "invoice")

File extension (.pdf, .png, etc.)

You can extend this to analyze file contents, not just names.
