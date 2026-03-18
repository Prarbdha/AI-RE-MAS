from agents.llm import llm, call_with_retry
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from schemas.models import REState

VALIDATION_PROMPT = """
You are a senior software architect reviewing requirements.
Analyze the following requirements and identify:
1. Ambiguous requirements (unclear/vague)
2. Missing critical information
3. Any contradictions

Return ONLY valid JSON:
{{
  "validation_notes": ["note1", "note2", ...],
  "ambiguities": ["ambiguity1", ...]
}}

Functional Requirements: {functional}
Non-Functional Requirements: {non_functional}
"""

def validation_agent(state: REState) -> REState:
    prompt = ChatPromptTemplate.from_template(VALIDATION_PROMPT)
    chain = prompt | llm | JsonOutputParser()

    result = call_with_retry(chain, {
        "functional": state.functional_reqs,
        "non_functional": state.non_functional_reqs
    })

    state.validation_notes = result.get("validation_notes", [])
    state.ambiguities = result.get("ambiguities", [])

    print(f"[Validation] {len(state.ambiguities)} ambiguities found.")
    return state