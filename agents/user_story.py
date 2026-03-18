from agents.llm import llm, call_with_retry     
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from schemas.models import REState

USER_STORY_PROMPT = """
Convert the following functional requirements into Agile user stories.
Each story must follow: "As a [user], I want [goal], so that [benefit]."
Include acceptance criteria for each.

Return ONLY valid JSON:
{{
  "user_stories": [
    {{
      "story": "As a ...",
      "acceptance_criteria": ["criterion1", "criterion2"]
    }}
  ]
}}

Requirements: {functional}
"""

def user_story_agent(state: REState) -> REState:
    prompt = ChatPromptTemplate.from_template(USER_STORY_PROMPT)
    chain = prompt | llm | JsonOutputParser()

    result =   call_with_retry(chain, {"functional": state.functional_reqs})
    stories = result.get("user_stories", [])

    # Flatten to strings for state
    state.user_stories = [
        f"{s['story']}\nAcceptance Criteria:\n" +
        "\n".join(f"  - {c}" for c in s.get("acceptance_criteria", []))
        for s in stories
    ]

    print(f"[User Story] {len(state.user_stories)} stories generated.")
    return state