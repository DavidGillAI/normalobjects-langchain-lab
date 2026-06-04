from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)

from langchain.tools import tool
import random

@tool
def consult_demogorgon(complaint: str) -> str:
    """Get the Demogorgon's perspective on a complaint."""
    
    responses = [
        f"The Demogorgon seems puzzled by '{complaint}'.",
        f"The Demogorgon growls thoughtfully about '{complaint}'.",
        f"The Demogorgon ignores '{complaint}' and wanders off."
    ]

    return random.choice(responses)

print(
    consult_demogorgon.invoke("Why do demogorgons sometimes eat people and sometimes don't?"
                              ))

@tool
def ask_NDGT(question: str) -> str:
    """Ask Neil DeGrasse Tyson for a scientific perspective."""

    return (
        f"NDGT adjusts his waistcoat and considers '{question}'. "
        "The answer likely involves physics, biology, chemistry, "
        "or a misunderstanding of how the universe actually works."
    )

print(
    ask_NDGT.invoke(
        "Why do creatures and power lines react strangely together?"
    )
)