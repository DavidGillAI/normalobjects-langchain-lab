# NormalObjects LangChain Complaint Handler

A creative complaint-handling agent built using LangChain and OpenAI.

## Features

* Custom Demogorgon consultation tool
* NDGT (Neil DeGrasse Tyson-inspired) science tool
* Alan Watts-inspired philosophy tool
* Flexible tool chaining using a LangChain agent
* Creative responses to complaints from the Normal Objects universe

## Files

* `normalobjects_langchain.py` - Main application
* `lab_summary.md` - Reflection and comparison with structured workflows
* `demo_output.txt` - Example agent responses
* `README.md` - Project documentation

## Installation

```bash
pip install langchain langchain-openai python-dotenv
```

## Setup

Create a `.env` file containing:

```text
OPENAI_API_KEY=your_api_key_here
```

## Run

```bash
python normalobjects_langchain.py
```

## Example Complaints

* Why do demogorgons sometimes eat people and sometimes don't?
* The portal appears to violate the laws of thermodynamics.
* Why do creatures and power lines react strangely together?

The agent selects and combines expert tools as needed to generate creative responses.
