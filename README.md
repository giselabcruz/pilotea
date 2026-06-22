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
1. **Environment**:
   ```bash
   pip install -e .
   ```
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
   ```bash
   python src/pilotea/main.py
   ```
