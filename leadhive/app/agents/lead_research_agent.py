from groq import Groq
from ..utils import clean_text

MODEL_NAME = "llama-3.3-70b-versatile"

class LeadResearchAgent:
    """
    Generates initial lead candidates based on:
    - Industry
    - Persona/Role
    - Region
    - Lead count

    This simulates a lead research/scraping step using the LLM.
    """

    def __init__(self, api_key: str):
        self.client = Groq(api_key=api_key)

    def run(self, industry: str, persona: str, region: str, lead_count: int = 5) -> dict:
        industry = clean_text(industry)
        persona = clean_text(persona)
        region = clean_text(region)

        prompt = f"""
        You are the LEAD RESEARCH AGENT in a business intelligence system.

        Your task:
        - Generate a list of {lead_count} potential leads.
        - Leads must belong to the industry: "{industry}"
        - Leads must match the persona/role: "{persona}"
        - Region focus (if any): "{region}"

        For each lead, return:
        - Full Name
        - Role/Title
        - Company Name
        - One-line company description

        Output format:
        ---
        LEADS:
        - name: ...
          role: ...
          company: ...
          company_desc: ...
        ---
        """

        response = self.client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}]
        )

        content = response.choices[0].message.content
        return {"raw_leads": content}
