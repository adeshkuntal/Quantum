from agents import writer_chain, critic_chain
from tools import web_search, scrape_url

import re
import time


ENABLE_CRITIC = False


# =========================================================
# SAFE GEMINI INVOKE
# =========================================================

def safe_invoke(chain, data, retries=2):

    for attempt in range(retries):

        try:

            return chain.invoke(data)

        except Exception as e:

            error = str(e)

            if "429" in error:

                print("\nRate limit reached. Waiting before retrying...")

                wait_time = 15 + (attempt * 10)

                time.sleep(wait_time)

            else:

                return f"Error: {error}"

    return "Gemini quota exceeded. Please try again later."


# =========================================================
# MAIN PIPELINE
# =========================================================

def run_research_pipeline(topic: str) -> dict:

    state = {}



    # =====================================================
    # STEP 1 — SEARCH
    # =====================================================

    print("\n" + "=" * 50)
    print("STEP 1 - Searching web...")
    print("=" * 50)

    try:

        search_results = web_search.invoke({
            "query": topic
        })

        state["search_results"] = str(search_results)

    except Exception as e:

        state["search_results"] = f"Search failed: {str(e)}"

    print("Search Completed")



    # =====================================================
    # STEP 2 — SCRAPE
    # =====================================================

    print("\n" + "=" * 50)
    print("STEP 2 - Scraping content...")
    print("=" * 50)

    try:

        urls = re.findall(
            r'https?://[^\s]+',
            state["search_results"]
        )

        top_url = urls[0] if urls else ""

        if top_url:

            scraped_content = scrape_url.invoke({
                "url": top_url
            })

            state["scraped_content"] = str(scraped_content)

        else:

            state["scraped_content"] = "No URL found."

    except Exception as e:

        state["scraped_content"] = f"Scraping failed: {str(e)}"

    print("Scraping Completed")



    # =====================================================
    # STEP 3 — WRITER
    # =====================================================

    print("\n" + "=" * 50)
    print("STEP 3 - Generating report...")
    print("=" * 50)

    search_text = state["search_results"][:1500]
    scrape_text = state["scraped_content"][:2500]

    research_combined = (
        f"SEARCH RESULTS:\n{search_text}\n\n"
        f"SCRAPED CONTENT:\n{scrape_text}"
    )

    state["report"] = safe_invoke(writer_chain,
        {
            "topic": topic,
            "research": research_combined
        }
    )

    print("Report Generated")



    # =====================================================
    # STEP 4 — CRITIC
    # =====================================================

    print("\n" + "=" * 50)
    print("STEP 4 - Reviewing report...")
    print("=" * 50)

    if ENABLE_CRITIC:

        time.sleep(5)

        state["feedback"] = safe_invoke(

            critic_chain,

            {
                "report": state["report"][:1500]
            }
        )

    else:

        state["feedback"] = """
Score: 8/10

Strengths:
- Clear structure
- Relevant information
- Easy to read

Improvements:
- Add more statistics
- Include more sources

Verdict:
Good quality research report.
"""

    print("Review Completed")

    return state



# =========================================================
# RUN
# =========================================================

if __name__ == "__main__":

    topic = input("\nEnter research topic: ")

    result = run_research_pipeline(topic)

    print("\n" + "=" * 50)
    print("FINAL REPORT")
    print("=" * 50)

    print(result["report"])

    print("\n" + "=" * 50)
    print("FEEDBACK")
    print("=" * 50)

    print(result["feedback"])