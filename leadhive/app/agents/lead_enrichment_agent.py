from groq import Groq
from ..utils import clean_text

MODEL_NAME = "llama-3.3-70b-versatile"

class LeadEnrichmentAgent:
    """
    Enriches each raw lead with:
    - Pain points
    - Role/industry challenges
    - Company context
    - Buying signal
    - Relevance score
    - Fit summary
    """

    def __init__(self, api_key: str):
        self.client = Groq(api_key=api_key)

    def run(self, raw_leads: str) -> dict:
        raw_leads = clean_text(raw_leads)

        prompt = f"""
        You are the LEAD ENRICHMENT AGENT in a sales intelligence system.

        Using ONLY the raw lead data below, enrich each lead with:
        - 3 pain points relevant to their role
        - Key responsibilities
        - One buying intent signal
        - Estimated budget level (low/medium/high)
        - A relevance/fit score from 0.0 to 1.0
        - A short fit summary

        Raw Leads:
        {raw_leads}

        Return output in this EXACT format:
        ---
        ENRICHED_LEADS:
        - name: ...
          role: ...
          company: ...
          company_desc: ...
          pain_points:
            - ...
            - ...
            - ...
          buying_intent: ...
          budget_level: ...
          relevance_score: ...
          fit_summary: ...
        ---
        """

        response = self.client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}]
        )

        content = response.choices[0].message.content
        return {"enriched_leads": content}
