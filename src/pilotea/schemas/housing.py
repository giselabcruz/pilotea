from pydantic import BaseModel, Field
from typing import List, Optional

class FinancialRequirement(BaseModel):
    item: str = Field(description="Name of the financial requirement (e.g. Deposit, Mortgage, Taxes)")
    description: str = Field(description="Detailed explanation of the requirement")
    estimated_cost: Optional[str] = Field(description="Estimated cost or percentage (if applicable)")

class LegalRequirement(BaseModel):
    document: str = Field(description="Name of the document or legal step (e.g. NIE, Bank Account, Arras)")
    description: str = Field(description="What is this document for and how to get it")

class HousingStep(BaseModel):
    order: int
    title: str
    action: str = Field(description="The specific action the user needs to take")

class HousingResponse(BaseModel):
    summary: str = Field(description="High-level overview of the process")
    financial_requirements: List[FinancialRequirement]
    legal_requirements: List[LegalRequirement]
    roadmap: List[HousingStep] = Field(description="Step-by-step guide to buying the house")
    additional_tips: List[str]
