from langgraph.graph import StateGraph, END
from schemas.models import REState
from agents.ingestion import ingestion_agent
from agents.extraction import extraction_agent
from agents.validation import validation_agent
from agents.srs_generator import srs_agent
from agents.user_story import user_story_agent

def build_pipeline():
    graph = StateGraph(REState)

    graph.add_node("ingest", ingestion_agent)
    graph.add_node("extract", extraction_agent)
    graph.add_node("validate", validation_agent)
    graph.add_node("srs", srs_agent)
    graph.add_node("stories", user_story_agent)

    graph.set_entry_point("ingest")
    graph.add_edge("ingest", "extract")
    graph.add_edge("extract", "validate")
    graph.add_edge("validate", "srs")
    graph.add_edge("srs", "stories")
    graph.add_edge("stories", END)

    return graph.compile()