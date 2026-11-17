
# AI Memory Chatbot

## Project Overview
AI Memory Chatbot is a Python-based conversational AI application that uses short-term and long-term memory to maintain context across conversations.

## Technologies Used
- Python
- Streamlit
- Ollama
- Qwen 2.5 Coder 7B
- SQLite

## Features
1. Short-term conversation memory.
2. Long-term memory using SQLite.
3. Persistent memory across application restarts.
4. Save important information using the `Remember:` command.
5. View saved memories.
6. Update saved memories.
7. Delete all saved memories.

## Project Structure

```text
AI-chatbot/
│
├── app.py
├── memory.py
├── llm.py
├── memory.db
├── requirements.txt
├── architecture.md
├── memory_chatbot.png
└── architecture_diagram.png
```

## Installation

1. Install Python.
2. Install Ollama.
3. Pull the model:

```bash
ollama pull qwen2.5-coder:7b
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
streamlit run app.py
```

## How to Save a Memory

Type a message beginning with:

```text
Remember: I am learning Python.
```

The chatbot saves the information in its SQLite database.

## Memory Management
Users can view, update, and delete saved memories through the sidebar.

## Author
AI Memory Chatbot Project
