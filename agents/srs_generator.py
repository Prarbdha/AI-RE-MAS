from agents.llm import llm, call_with_retry
from langchain_core.prompts import ChatPromptTemplate
from schemas.models import REState

SRS_PROMPT = """
You are a technical writer. Generate a complete IEEE 830-style SRS document
based on the requirements below. Use markdown formatting with these sections:
1. Introduction
2. Overall Description
3. Functional Requirements
4. Non-Functional Requirements
5. Constraints & Assumptions

Functional: {functional}
Non-Functional: {non_functional}
Validation Notes (known gaps to address):
{notes_formatted}
"""

def srs_agent(state: REState) -> REState:
    prompt = ChatPromptTemplate.from_template(SRS_PROMPT)
    chain = prompt | llm

    result = call_with_retry(chain, {
        "functional": state.functional_reqs,
        "non_functional": state.non_functional_reqs,
        "notes_formatted": "\n".join(f"- {n}" for n in state.validation_notes)
    })

    state.srs_document = result.content
    print("[SRS Generator] SRS document created.")
    return state