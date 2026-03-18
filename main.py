from graph.pipeline import build_pipeline
from schemas.models import REState

pipeline = build_pipeline()

# Test with plain text
initial_state = REState(
    raw_input="The system shall allow users to register and login. It must handle 1000 concurrent users. Response time should be under 2 seconds.",
    file_type="text"
)

final_state = pipeline.invoke(initial_state)

print("\n--- SRS DOCUMENT ---")
print(final_state["srs_document"])

print("\n--- USER STORIES ---")
for story in final_state["user_stories"]:
    print(story)
    print("---")