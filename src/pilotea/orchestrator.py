import os
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field
from pydantic_ai import Agent, RunContext
from src.pilotea.agents.housing import HousingAgent

class RoutingResult(BaseModel):
    agent_type: str = Field(description="The type of agent to handle the request (e.g. 'housing', 'tax', 'finance')")
    reasoning: str = Field(description="Why this agent was chosen")

class PiloteaOrchestrator:
    """
    Main entry point for Pilotea.
    Routes user queries to the appropriate domain-specific agent.
    """
    def __init__(self, model_name: Optional[str] = None):
        self.model_name = model_name or os.getenv("PILOTEA_MODEL", "openai:gpt-4o")
        
        self.router = Agent(
            self.model_name,
            result_type=RoutingResult,
            system_prompt=(
                "You are the Pilotea Router. Your job is to analyze the user's request "
                "and route it to the correct specialized agent. "
                "Current available agents: "
                "- 'housing': For any questions related to buying, renting, or property bureaucracy in Spain. "
                "- 'tax' (coming soon): For tax-related questions. "
                "- 'finance' (coming soon): For general personal finance or payslip questions. "
                "If the topic is not covered yet, still categorize it into the closest one or "
                "recommend 'housing' if it's the only one available for now."
            )
        )
        self.agents = {
            "housing": HousingAgent(self.model_name)
        }

    async def handle_query(self, query: str) -> Any:
        """Route the query and return the result from the specialized agent."""
        routing = await self.router.run(query)
        agent_type = routing.data.agent_type
        
        if agent_type in self.agents:
            agent = self.agents[agent_type]
            return await agent.run(query)
        else:
            return await self.agents["housing"].run(query)
