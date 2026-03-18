from pydantic import BaseModel, Field
from typing import List

class REState(BaseModel):
    raw_input: str = ""
    file_type: str = "text"           # text | pdf | image
    clean_text: str = ""
    functional_reqs: List[str] = []
    non_functional_reqs: List[str] = []
    validation_notes: List[str] = []
    ambiguities: List[str] = []
    srs_document: str = ""
    user_stories: List[str] = []