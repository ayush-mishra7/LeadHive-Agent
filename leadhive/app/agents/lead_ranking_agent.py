from groq import Groq
from ..utils import clean_text, normalize_score

MODEL_NAME = "llama-3.3-70b-versatile"

class LeadRankingAgent:
    """
    Ranks enriched leads using:
    - Relevance score
    - Budget level
    - Role importance
    - Pain point severity
    - Buying intent
    """

    def __init__(self, api_key: str):
        self.client = Groq(api_key=api_key)

    def run(self, enriched_leads: str) -> dict:
        enriched_leads = clean_text(enriched_leads)

        prompt = f"""
        You are the LEAD RANKING AGENT in a sales automation system.

        Based on the enriched lead data below, rank leads by:
        - Relevance score
        - Budget level (low/medium/high)
        - Seniority & role importance
        - Pain point severity
        - Buying intent signals

        Assign each lead:
        - final_rank: integer (1 = highest priority)
        - priority_label: High / Medium / Low
        - value_score: 0.0–1.0
        - recommended_action: "Email", "LinkedIn Outreach", "Demo Request", etc.

        Enriched Leads:
        {enriched_leads}

        Return output in this EXACT format:
        ---
        RANKED_LEADS:
        - name: ...
          role: ...
          company: ...
          final_rank: ...
          priority_label: ...
          value_score: ...
          recommended_action: ...
        ---
        """

        response = self.client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}]
        )

        content = response.choices[0].message.content
        return {"ranked_leads": content}
