import os

folders = [
    "leadhive",
    "leadhive/app",
    "leadhive/app/agents"
]

files = [
    "leadhive/requirements.txt",
    "leadhive/Dockerfile",
    "leadhive/README.md",
    "leadhive/app/main.py",
    "leadhive/app/utils.py",
    "leadhive/app/models.py",
    "leadhive/app/agents/lead_research_agent.py",
    "leadhive/app/agents/lead_enrichment_agent.py",
    "leadhive/app/agents/lead_ranking_agent.py",
    "leadhive/app/agents/outreach_agent.py",
    "leadhive/app/agents/orchestrator.py"
]

def create_project():
    print("Creating LeadHive Agent System project...\n")

    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Created folder: {folder}")

    for file in files:
        with open(file, "w") as f:
            pass
        print(f"Created empty file: {file}")

    print("\nLeadHive project structure created successfully!")

if __name__ == "__main__":
    create_project()
