# LeadHive AI – Automated Lead Generation & Outreach Agent System

LeadHive is a multi-agent AI system that automates **lead generation, enrichment, ranking, and personalized outreach**.  
It uses LLM-powered agents orchestrated through a FastAPI backend to simulate a complete AI-driven sales intelligence workflow.

Built for **portfolio quality**, this project demonstrates:
- Multi-agent orchestration  
- Practical LLM automation  
- Lead generation workflows  
- Sales intelligence logic  
- Backend development  
- Prompt engineering  

---

## 🚀 Features

### 🔍 Lead Research Agent
Generates raw lead candidates (name, role, company, description) based on:
- Industry  
- Persona  
- Region  

### 🧩 Lead Enrichment Agent
Adds:
- Pain points  
- Role challenges  
- Budget level  
- Buying signals  
- Relevance score  
- Fit summary  

### 🔢 Lead Ranking Agent
Prioritizes leads using:
- Relevance score  
- Seniority  
- Budget  
- Buying intent  
- Pain point severity  

### ✉️ Outreach Agent
Generates personalized outreach messages:
- Email  
- LinkedIn message  
- Short DM pitch  
- CTA-based messages  

### 🤖 Orchestrator Agent
Runs all agents in sequence and returns a unified lead generation + outreach plan.

---

## 📁 Project Structure

leadhive/
│── requirements.txt
│── Dockerfile
│── README.md
│── .env # contains GROQ_API_KEY
│── app/
│ ├── main.py
│ ├── utils.py
│ ├── models.py
│ └── agents/
│ ├── lead_research_agent.py
│ ├── lead_enrichment_agent.py
│ ├── lead_ranking_agent.py
│ ├── outreach_agent.py
│ └── orchestrator.py


---

## 🔧 Installation

### 1️⃣ Create environment
```bash
conda create -n leadhive python=3.10 -y
conda activate leadhive
```
### 2️⃣ Install requirements
```bash
pip install -r requirements.txt
```
### 3️⃣ Add Groq API Key
Create .env inside the leadhive root:
```bash
GROQ_API_KEY=your_actual_key_here
```
### ▶️ Run the Backend
```bash
uvicorn app.main:app --reload
```
### Open API docs:
👉 http://127.0.0.1:8000/docs

### Example input
```bash
{
  "industry": "SaaS Analytics",
  "persona": "Head of Product",
  "region": "USA",
  "lead_count": 5,
  "outreach_style": "email"
}
```
### 🐳 Run with Docker
Build image:
```bash
docker build -t leadhive .
```
Run container:
```bash
docker run -p 8000:8000 -e GROQ_API_KEY=your_key_here leadhive
```
### 🧠 Tech Stack
- Python
- FastAPI
- Groq LLaMA Models
- Agentic AI architecture
- Docker
- Pydantic
- dotenv

### 🎯 Ideal For
- AI Engineer / ML Engineer portfolios
- Agent-based AI projects
- Sales automation use-cases
- Demonstrating LLM pipelines
- Real-world business impact projects

### 👤 Author

Ayush Mishra

GitHub: @ayush-mishra7

LinkedIn: @ayushmishra77