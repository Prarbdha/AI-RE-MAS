import fitz  # PyMuPDF
import pytesseract
from PIL import Image
from schemas.models import REState

def ingestion_agent(state: REState) -> REState:
    file_type = state.file_type
    raw = state.raw_input

    if file_type == "text":
        state.clean_text = raw.strip()

    elif file_type == "pdf":
        # raw_input = file path to PDF
        doc = fitz.open(raw)
        text = ""
        for page in doc:
            text += page.get_text()
        state.clean_text = text.strip()

    elif file_type == "image":
        # raw_input = file path to image
        img = Image.open(raw)
        state.clean_text = pytesseract.image_to_string(img).strip()

    print(f"[Ingestion] Extracted {len(state.clean_text)} characters.")
    return state