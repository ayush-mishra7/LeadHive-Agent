from groq import Groq
from ..utils import clean_text

MODEL_NAME = "llama-3.3-70b-versatile"

class OutreachAgent:
    """
    Generates personalized outreach messages based on enriched + ranked leads.
    Supports:
    - Professional Email
    - LinkedIn Message
    - Short DM Pitch
    """

    def __init__(self, api_key: str):
        self.client = Groq(api_key=api_key)

    def run(self, ranked_leads: str, outreach_style: str = "email") -> dict:
        ranked_leads = clean_text(ranked_leads)

        prompt = f"""
        You are the OUTREACH AGENT in an automated lead-generation system.

        Using ONLY the ranked lead data below, generate personalized outreach messages.

        Outreach Style Requested: "{outreach_style}"

        For each lead, generate:
        - A personalized opener referencing role/company
        - A value-driven pitch aligned with their pain points
        - A CTA (Call To Action) suited to the style

        Output formats based on outreach_style:

        1. "email":
            - subject: ...
            - message: ...

        2. "linkedin":
            - message: ...

        3. "short_dm":
            - message: (2–3 lines only)

        Input Ranked Leads:
        {ranked_leads}

        Return output in EXACT format:
        ---
        OUTREACH_MESSAGES:
        - name: ...
          role: ...
          company: ...
          style: "{outreach_style}"
          subject: ...
          message: ...
        ---
        """

        response = self.client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}]
        )

        content = response.choices[0].message.content
        return {"outreach_messages": content}
