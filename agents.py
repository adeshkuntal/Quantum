from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()


# =========================================================
# MODEL SETUP
# =========================================================

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-lite",
    temperature=0,
)


# =========================================================
# WRITER CHAIN
# =========================================================

writer_prompt = ChatPromptTemplate.from_messages([

    (
        "system",
        "You are a professional research writer. "
        "Write concise, clear and factual reports."
    ),

    (
        "human",
        """
        Write a research report on:

        Topic:
        {topic}

        Research:
        {research}

        Structure:
        1. Introduction
        2. Key Findings
        3. Conclusion
        4. Sources

        Keep the report under 500 words.
        """
    ),
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