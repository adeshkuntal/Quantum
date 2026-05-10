from langchain.tools import tool
from tavily import TavilyClient
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from rich import print
import requests
import os
load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

# First Tool to get live web results
@tool
def web_search(query : str) -> str:
    """Search the web for recent and reliable information on a topic . Returns Titles , URLs and snippets."""
    try:
        results = tavily.search(
            query=query[:300],
            max_results=3,
            timeout=20
        )

        formatted = []

        for r in results.get("results", []):
            formatted.append(
                f"Title: {r.get('title')}\n"
                f"URL: {r.get('url')}\n"
                f"Content: {r.get('content')}\n"
            )

        return "\n\n".join(formatted)

    except Exception as e:
        return f"Search failed: {str(e)}"

# print(web_search.invoke("what are the recent news of war?"))



# Second tool to scrape or get text from web data
@tool
def scrape_url(url: str) -> str:
    """Scrape and return clean text content from a given URL for deeper reading."""
    try:
        resp = requests.get(
            url,
            timeout=8,
            headers={"User-Agent": "Mozilla/5.0"}
        )
        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()
        return soup.get_text(separator=" ", strip=True)[:3000]
    
    except Exception as e:
        return f"Could not scrape URL: {str(e)}"
    
# print(scrape_url.invoke("https://www.war.gov/news/"))
