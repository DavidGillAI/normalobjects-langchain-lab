from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_agent
from langchain.tools import tool
import random

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)



@tool
def consult_demogorgon(complaint: str) -> str:
    """Get the Demogorgon's perspective on a complaint."""
    
    responses = [
        f"The Demogorgon seems puzzled by '{complaint}'.",
        f"The Demogorgon growls thoughtfully about '{complaint}'.",
        f"The Demogorgon ignores '{complaint}' and wanders off."
    ]

    return random.choice(responses)

@tool
def ask_NDGT(question: str) -> str:
    """Ask Neil DeGrasse Tyson for a scientific perspective."""

    return (
        f"NDGT adjusts his waistcoat and considers '{question}'. "
        "The answer likely involves physics, biology, chemistry, "
        "or a misunderstanding of how the universe actually works."
    )

tools = [
    consult_demogorgon,
    ask_NDGT
]

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=(
        "You are a creative complaint handler for the Normal Objects universe."
        "Investigate unusual complaints using the tools available to you."
        "You may consult one or more experts before providing a final answer."
        "Be imaginative, helpful, and entertaining."
    )
)

complaints = [
    "The portal appears to violate the laws of thermodynamics.",
    "Why do demogorgons sometimes eat people and sometimes don't?",
    "Why do creatures and power lines react strangely together?"
]

for complaint in complaints:
    print("\n" + "=" * 60)
    print(f"COMPLAINT: {complaint}")
    print("=" * 60)

    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": complaint
                }
            ]
        }
    )

    print(response["messages"][-1].content)