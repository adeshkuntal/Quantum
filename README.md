Quantum — AI Multi-Agent Research System

An intelligent AI-powered research assistant built using Streamlit, LangChain, Gemini API, Tavily Search, and BeautifulSoup.
Quantum automates the complete research workflow — from searching the web to generating structured AI research reports.

Features
AI-powered research report generation
Real-time web search using Tavily API
Web scraping using BeautifulSoup
Streamlit-based modern UI
Multi-step autonomous research pipeline
Structured report generation
Critic/review system for report evaluation
Fast and lightweight architecture
Gemini-powered reasoning and summarization
Tech Stack
Frontend
Streamlit
Backend
Python
AI / LLM
Google Gemini API
LangChain
Search & Scraping
Tavily Search API
BeautifulSoup
Requests
Architecture
User Query
    ↓
Tavily Web Search
    ↓
Web Scraping (BeautifulSoup)
    ↓
Gemini Writer Chain
    ↓
Research Report
    ↓
(Optional) Critic Review
Project Structure
Quantum/
│
├── app.py                # Streamlit frontend
├── pipeline.py           # Main research workflow
├── agents.py             # Gemini chains/prompts
├── tools.py              # Search + scraping tools
├── requirements.txt
├── .gitignore
└── README.md
Installation
Clone Repository
git clone https://github.com/adeshkuntal/Quantum.git

cd Quantum
Create Virtual Environment
Windows
python -m venv .venv

.venv\Scripts\activate
Linux / Mac
python3 -m venv .venv

source .venv/bin/activate
Install Dependencies
pip install -r requirements.txt
Environment Variables

Create a .env file in the root directory.

TAVILY_API_KEY=your_tavily_api_key

GEMINI_API_KEY=your_gemini_api_key
Run the Project
streamlit run app.py
Screenshots

Add your UI screenshots here after deployment.

assets/
├── home.png
├── pipeline.png
└── report.png
Deployment

The project is deployed using:

Streamlit Community Cloud
Optimization Highlights

This project is optimized to:

minimize Gemini API usage
reduce token consumption
avoid unnecessary LLM calls
improve research pipeline speed
handle API rate limits gracefully
Future Improvements
PDF export
Citation generation
Multi-source research comparison
Research memory/history
Async pipeline execution
Voice-based interaction
RAG integration
Vector database support
Author

Adesh Kumar
B.Tech CSE (AIML & IoT)
GLA University

GitHub:
Adesh Kuntal GitHub

License

This project is licensed under the MIT License.
