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
    """Ask NDGT for a scientific perspective on physics, biology, chemistry, or astrophysics."""

    question_lower = question.lower()

    if "thermodynamics" in question_lower or "energy" in question_lower:
        return (
            f"NDGT considers '{question}'. From a scientific perspective, "
            "a portal would need to account for conservation of energy, entropy, "
            "and the transfer of matter or information between two regions of spacetime."
        )

    if "power" in question_lower or "electric" in question_lower or "electromagnetic" in question_lower:
        return (
            f"NDGT considers '{question}'. Power lines create electromagnetic fields, "
            "and strange creatures may react to those fields through biology, magnetism, "
            "or sensory systems we do not fully understand."
        )

    if "creature" in question_lower or "monster" in question_lower:
        return (
            f"NDGT considers '{question}'. Creature behaviour usually comes down to biology: "
            "hunger, threat response, reproduction, environment, and available energy."
        )

    return (
        f"NDGT considers '{question}'. The answer likely involves physics, biology, "
        "chemistry, or a misunderstanding of how the universe actually works."
    )

@tool
def ask_alan_watts(question: str) -> str:
    """Ask Alan Watts for a philosophical and mystical perspective."""

    question_lower = question.lower()

    if "portal" in question_lower or "dimension" in question_lower:
        return (
            f"Alan Watts reflects on '{question}'. A portal is not merely a doorway "
            "between places, but a reminder that boundaries may be habits of perception. "
            "Perhaps the universe is not divided into here and there as neatly as we imagine."
        )

    if "monster" in question_lower or "creature" in question_lower or "demogorgon" in question_lower:
        return (
            f"Alan Watts reflects on '{question}'. The monster may be less an error in the world "
            "than a shadow we refuse to recognise. What appears threatening may simply be life "
            "wearing an unfamiliar mask."
        )

    if "power" in question_lower or "electric" in question_lower or "energy" in question_lower:
        return (
            f"Alan Watts reflects on '{question}'. Energy is not something separate from life, "
            "but the dance of life itself. Perhaps the strange reaction is not a malfunction, "
            "but a rhythm we have not yet learned to hear."
        )

    return (
        f"Alan Watts reflects on '{question}'. Perhaps the problem is not the inconsistency, "
        "but our demand that reality behave like a tidy machine. In the Normal Objects universe, "
        "contradiction may simply be the universe dancing in a mask."
    )


tools = [
    consult_demogorgon,
    ask_NDGT,
    ask_alan_watts
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
    "Why do creatures and power lines react strangely together?",
    "Why does the Upside Down feel more like a dream than a place?"
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