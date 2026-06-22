import asyncio
import os
from dotenv import load_dotenv
from src.pilotea.orchestrator import PiloteaOrchestrator

# Load environment variables
load_dotenv()

async def main():
    # Ensure environment variables are loaded
    load_dotenv()
    
    orchestrator = PiloteaOrchestrator()
    print(f"Using model: {orchestrator.model_name}")

    # Ensure API key is set if using OpenAI
    if "openai" in orchestrator.model_name and not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found in environment. Please set it in your .env file or switch to Ollama.")
        return

    question = "What do I need to buy my first house in Spain?"
    print(f"\n--- Pilotea Query: {question} ---\n")
    
    try:
        result = await orchestrator.handle_query(question)
        
        print(f"Summary: {result.summary}\n")
        
        print("--- Financial Requirements ---")
        for req in result.financial_requirements:
            print(f"- {req.item}: {req.description} ({req.estimated_cost})")
            
        print("\n--- Legal Requirements ---")
        for req in result.legal_requirements:
            print(f"- {req.document}: {req.description}")
            
        print("\n--- Step-by-Step Roadmap ---")
        for step in sorted(result.roadmap, key=lambda x: x.order):
            print(f"{step.order}. {step.title}: {step.action}")
            
        print("\n--- Additional Tips ---")
        for tip in result.additional_tips:
            print(f"- {tip}")
            
    except Exception as e:
        print(f"Error executing agent: {e}")

if __name__ == "__main__":
    asyncio.run(main())
