from pydantic import BaseModel
from typing import List, Optional


class LeadRequest(BaseModel):
    industry: str
    persona: str
    region: Optional[str] = "global"
    lead_count: Optional[int] = 5
    outreach_style: Optional[str] = "email"   # email, linkedin, short_dm


class Lead(BaseModel):
    name: str
    role: str
    company: str
    company_desc: str
    relevance_score: float
    pain_points: List[str]


class OutreachMessage(BaseModel):
    style: str
    message: str


class LeadHiveResponse(BaseModel):
    topic: str
    summary: str
    leads: List[Lead]
    outreach_messages: List[OutreachMessage]
