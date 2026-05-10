<div align="center">

<img src="https://img.shields.io/badge/Quantum-AI%20Research%20System-7c3aed?style=for-the-badge&logo=streamlit&logoColor=white" alt="Quantum Banner"/>

# ⚛ Quantum

### An AI-powered Multi-Agent Research System for autonomous web research and report generation.

[![Live Demo](https://img.shields.io/badge/🌐%20Live%20Demo-Quantum-purple?style=flat-square)](https://quantum-research-system.streamlit.app)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io)
[![LangChain](https://img.shields.io/badge/LangChain-AI-green?style=flat-square)](https://langchain.com)
[![Gemini](https://img.shields.io/badge/Gemini-Google%20AI-4285F4?style=flat-square&logo=google&logoColor=white)](https://ai.google.dev)
[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](#license)

</div>

---

# 📖 Table of Contents

- [About](#-about)
- [Live Demo](#-live-demo)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Architecture](#-architecture)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Environment Variables](#environment-variables)
  - [Installation](#installation)
- [Workflow](#-workflow)
- [Screenshots](#-screenshots)
- [Deployment](#-deployment)
- [Future Improvements](#-future-improvements)
- [Contributing](#-contributing)
- [License](#-license)

---

# 🌟 About

**Quantum** is an AI-powered autonomous research assistant that automates the complete research workflow using Large Language Models and web intelligence tools.

The system performs:
- real-time web research,
- intelligent content extraction,
- AI-powered summarization,
- and structured report generation.

Quantum combines:
- **Tavily Search API**
- **BeautifulSoup Web Scraping**
- **Google Gemini**
- **LangChain**
- **Streamlit**

to create a modern multi-agent research pipeline.

---

# 🌐 Live Demo

| Service | URL |
|----------|-----|
| 🚀 Streamlit App | https://quantum-research-system.streamlit.app |

---

# ✅ Features

- 🔍 Real-time web research using Tavily API
- 🌐 Intelligent webpage scraping using BeautifulSoup
- 🤖 Gemini-powered AI report generation
- 🧠 Multi-step autonomous research workflow
- 📄 Structured research reports
- 🎨 Modern Streamlit UI
- ⚡ Fast optimized architecture
- 🛡️ API rate-limit handling
- 📱 Responsive design
- ☁️ Streamlit Cloud deployment support

---

# 🛠️ Tech Stack

## Frontend

| Technology | Purpose |
|------------|---------|
| Streamlit | Interactive UI |
| HTML/CSS | Custom styling |

---

## Backend

| Technology | Purpose |
|------------|---------|
| Python | Core backend language |
| Requests | HTTP requests |
| BeautifulSoup | Web scraping |
| dotenv | Environment variables |

---

## AI / LLM

| Technology | Purpose |
|------------|---------|
| Google Gemini | AI report generation |
| LangChain | LLM orchestration |

---

## Search Engine

| Technology | Purpose |
|------------|---------|
| Tavily API | Real-time web search |

---

# 🧠 Architecture

```text
User Query
    ↓
Tavily Web Search
    ↓
Top URL Extraction
    ↓
BeautifulSoup Scraping
    ↓
Gemini Writer Chain
    ↓
Structured Research Report
    ↓
(Optional) Critic Review
```

---

# 📁 Project Structure

```text
Quantum/
│
├── app.py                 # Streamlit frontend
├── pipeline.py            # Main research pipeline
├── agents.py              # Gemini chains/prompts
├── tools.py               # Tavily + scraping tools
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 🚀 Getting Started

## Prerequisites

- Python 3.11+
- Tavily API Key
- Gemini API Key

---

## Environment Variables

Create a `.env` file in the root directory.

```env
TAVILY_API_KEY=your_tavily_api_key

GEMINI_API_KEY=your_gemini_api_key
```

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/adeshkuntal/Quantum.git

cd Quantum
```

---

### 2. Create Virtual Environment

#### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

#### Linux / Mac

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run Streamlit App

```bash
streamlit run app.py
```

---

# ⚙️ Workflow

## Step 1 — Web Search

Quantum searches the web using Tavily API to collect:
- titles
- URLs
- summaries
- latest information

---

## Step 2 — Web Scraping

The system extracts deep webpage content using:
- BeautifulSoup
- Requests

---

## Step 3 — AI Report Generation

Gemini generates:
- introduction
- key findings
- conclusion
- source summary

---

## Step 4 — Critic Review (Optional)

The AI critic reviews:
- report quality
- structure
- improvements
- final verdict

---

# 📸 Screenshots

Add your screenshots here.

```text
assets/
├── home.png
├── pipeline.png
└── report.png
```

---

# ☁️ Deployment

Quantum is deployed using:

- Streamlit Community Cloud

---

# 🚀 Future Improvements

- PDF export
- Citation generation
- Async pipeline execution
- Research history
- Multi-source comparison
- Voice input
- RAG integration
- Vector database support
- AI memory system

---

# 🤝 Contributing

Contributions are welcome!

### Steps:

1. Fork the repository
2. Create feature branch

```bash
git checkout -b feature/feature-name
```

3. Commit changes

```bash
git commit -m "feat: add new feature"
```

4. Push changes

```bash
git push origin feature/feature-name
```

5. Open Pull Request

---

# 👨‍💻 Author

## Adesh Kumar

B.Tech CSE (AIML & IoT)  
GLA University

GitHub:  
https://github.com/adeshkuntal

---

# 📄 License

This project is licensed under the MIT License.

---

<div align="center">

Made with ❤️ using Streamlit, Gemini & LangChain

</div>
