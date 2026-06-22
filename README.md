# Pilotea
AI-powered guide for life administration and personal procedures.

## How it works
Introduce your problem, the AI agent will route you to a specialized domain agent, and then provide you with a structured guide to solve it.

### MVP1: Housing Agent (Spain)
- "What do I need to buy my first house in Spain?"
- The agent provides financial requirements, legal documents, and a step-by-step roadmap.

## Project Structure (Clean Architecture)
```
pilotea/
├── src/
│   └── pilotea/
│       ├── main.py            # Entry point
│       ├── orchestrator.py     # Routing logic
│       ├── agents/             # Specialized agents (Housing)
│       ├── tools/              # Reusable tools (Search)
│       └── schemas/            # Structured data models
└── pyproject.toml
```

## Setup
1. **Quick Setup (Recommended)**:
   bash setup.sh
   source venv/bin/activate
   ```
2. **Manual Environment**:
    For manual setup, you need to install the dependencies in a virtual environment.

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -e .
   
2. **Configuration**:
   Copy `.env.example` to `.env`.
   - **For OpenAI**: Add your `OPENAI_API_KEY` and set `PILOTEA_MODEL=openai:gpt-4o`.
   - **For Ollama (Free/Local)**: Set `PILOTEA_MODEL=ollama:llama3.1`.
     - **Instalación de Ollama**:
       1. Descarga e instala Ollama desde [ollama.com](https://ollama.com).
       2. Descarga e inicia el modelo ejecutando en tu terminal:
          ```bash
          ollama run llama3.1
          ```
3. **Run**:
   - **CLI Mode**:
     ```bash
     python src/pilotea/main.py
     ```
   - **Web UI Mode** (Recommended):
     ```bash
     python src/pilotea/api.py
     ```
     Then open [http://localhost:8000](http://localhost:8000) in your browser.
