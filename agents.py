from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()


# =========================================================
# MODEL SETUP
# =========================================================

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)


# =========================================================
# WRITER CHAIN
# =========================================================

writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Write clear, structured and insightful reports."),
    ("human", """Write a detailed research report on the topic below.

    Topic: {topic}

    Research Gathered:
    {research}

    Structure the report as:
    - Introduction
    - Key Findings (minimum 3 well-explained points)
    - Conclusion
    - Sources (list all URLs found in the research)

    Be detailed, factual and professional."""),
])

writer_chain = writer_prompt | llm | StrOutputParser()


# =========================================================
# CRITIC CHAIN
# =========================================================

critic_prompt = ChatPromptTemplate.from_messages([

    (
        "system",
        "You are a concise research reviewer."
    ),

    (
        "human",
        """
        Review this report briefly.

        Report:
        {report}

        Give:

        Score: X/10

        Strengths:
        - ...

        Improvements:
        - ...

        Verdict:
        ...
        """
    ),
])

critic_chain = critic_prompt | llm | StrOutputParser()