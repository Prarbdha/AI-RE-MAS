from agents.llm import llm, call_with_retry
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from schemas.models import REState

EXTRACTION_PROMPT = """
You are a requirements engineering expert.
Given the following unstructured input, extract all software requirements.

Return ONLY valid JSON in this format:
{{
  "functional": ["req1", "req2", ...],
  "non_functional": ["req1", "req2", ...]
}}

Input:
{text}
"""

def extraction_agent(state: REState) -> REState:
    prompt = ChatPromptTemplate.from_template(EXTRACTION_PROMPT)
    chain = prompt | llm | JsonOutputParser()

    result = call_with_retry(chain, {"text": state.clean_text})

    state.functional_reqs = result.get("functional", [])
    state.non_functional_reqs = result.get("non_functional", [])

    print(f"[Extraction] Found {len(state.functional_reqs)} functional, {len(state.non_functional_reqs)} non-functional reqs.")
    return state