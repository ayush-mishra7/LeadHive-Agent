from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os

from .agents.orchestrator import Orchestrator

app = FastAPI(title="LeadHive AI – Automated Lead Generation & Outreach System")

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env file. Please add it.")

# Initialize Orchestrator
orchestrator = Orchestrator(api_key=API_KEY)


# ----------- Request Schema -----------
class LeadRequest(BaseModel):
    industry: str
    persona: str
    region: str = "global"
    lead_count: int = 5
    outreach_style: str = "email"  # email, linkedin, short_dm


# ----------- Endpoint -----------
@app.post("/generate-leads")
async def generate_leads(req: LeadRequest):
    """
    Generates:
    1. Raw Leads
    2. Enriched Leads
    3. Ranked Leads
    4. Outreach Messages

    using the full multi-agent LeadHive pipeline.
    """

    result = orchestrator.run(
        industry=req.industry,
        persona=req.persona,
        region=req.region,
        lead_count=req.lead_count,
        outreach_style=req.outreach_style,
    )

    return {
        "industry": req.industry,
        "persona": req.persona,
        "region": req.region,
        "lead_count": req.lead_count,
        "outreach_style": req.outreach_style,
        "raw_leads": result["raw_leads"],
        "enriched_leads": result["enriched_leads"],
        "ranked_leads": result["ranked_leads"],
        "outreach_messages": result["outreach_messages"]
    }
