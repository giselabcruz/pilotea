import os
from typing import Generic, TypeVar, Optional, Any
from pydantic import BaseModel
from pydantic_ai import Agent, RunContext
from abc import ABC, abstractmethod

T = TypeVar('T', bound=BaseModel)

class BaseAgent(ABC, Generic[T]):
    """
    Base class for all Pilotea agents.
    Provides a standardized way to define agents, tools, and system prompts.
    """
    def __init__(self, model_name: Optional[str] = None):
        # Use provided model_name, or default to PILOTEA_MODEL, or fallback to gpt-4o
        self.model_name = model_name or os.getenv("PILOTEA_MODEL", "openai:gpt-4o")
        
        self.agent = Agent(
            self.model_name,
            output_type=self.get_result_schema(),
            system_prompt=self.get_system_prompt(),
        )
        self.register_tools()

    @abstractmethod
    def get_system_prompt(self) -> str:
        """Define the agent's identity and instructions."""
        pass

    @abstractmethod
    def get_result_schema(self) -> type[T]:
        """Define the structured output for the agent."""
        pass

    def register_tools(self):
        """Register tools for this agent."""
        pass

    async def run(self, user_input: str, deps: Any = None) -> T:
        """Execute the agent run."""
        result = await self.agent.run(user_input, deps=deps)
        return result.output
