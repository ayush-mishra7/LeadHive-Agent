from .lead_research_agent import LeadResearchAgent
from .lead_enrichment_agent import LeadEnrichmentAgent
from .lead_ranking_agent import LeadRankingAgent
from .outreach_agent import OutreachAgent


class Orchestrator:
    """
    The central controller that orchestrates all 4 agents:
    1. Lead Research
    2. Lead Enrichment
    3. Lead Ranking
    4. Outreach Message Generation

    Returns a unified final output for the API.
    """

    def __init__(self, api_key: str):
        self.research_agent = LeadResearchAgent(api_key)
        self.enrichment_agent = LeadEnrichmentAgent(api_key)
        self.ranking_agent = LeadRankingAgent(api_key)
        self.outreach_agent = OutreachAgent(api_key)

    def run(self, industry: str, persona: str, region: str, lead_count: int, outreach_style: str):
        """
        Full automation pipeline.
        """

        # 1️⃣ Get raw leads
        raw_leads_output = self.research_agent.run(industry, persona, region, lead_count)
        raw_leads = raw_leads_output["raw_leads"]

        # 2️⃣ Enrich leads
        enriched_output = self.enrichment_agent.run(raw_leads)
        enriched_leads = enriched_output["enriched_leads"]

        # 3️⃣ Rank leads
        ranked_output = self.ranking_agent.run(enriched_leads)
        ranked_leads = ranked_output["ranked_leads"]

        # 4️⃣ Generate outreach messages
        outreach_output = self.outreach_agent.run(ranked_leads, outreach_style)
        outreach_messages = outreach_output["outreach_messages"]

        # Complete dataset returned to API
        return {
            "raw_leads": raw_leads,
            "enriched_leads": enriched_leads,
            "ranked_leads": ranked_leads,
            "outreach_messages": outreach_messages
        }
