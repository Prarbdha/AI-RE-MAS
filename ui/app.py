import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from graph.pipeline import build_pipeline
from schemas.models import REState

st.set_page_config(page_title="AI-RE-MAS", layout="wide")
st.title("🤖 AI Requirement Engineering Multi-Agent System")

pipeline = build_pipeline()

# Input section
st.subheader("📥 Input")
input_type = st.selectbox("Input Type", ["text", "pdf", "image"])

if input_type == "text":
    user_input = st.text_area("Paste your requirements or project description:", height=200)
    file_path = None
else:
    uploaded = st.file_uploader("Upload file", type=["pdf", "png", "jpg"])
    user_input = None
    file_path = None
    if uploaded:
        save_path = f"uploads/{uploaded.name}"
        with open(save_path, "wb") as f:
            f.write(uploaded.read())
        file_path = save_path

if st.button("🚀 Generate Artifacts"):
    with st.spinner("Running agents..."):
        state = REState(
            raw_input=user_input if input_type == "text" else file_path,
            file_type=input_type
        )
        result = pipeline.invoke(state)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📄 SRS Document")
        st.markdown(result["srs_document"])
        st.download_button("⬇️ Download SRS", result["srs_document"], "srs.md")

    with col2:
        st.subheader("📋 User Stories")
        for i, story in enumerate(result["user_stories"], 1):
            with st.expander(f"Story {i}"):
                st.text(story)

    if result["ambiguities"]:
        st.warning("⚠️ Ambiguities Detected")
        for a in result["ambiguities"]:
            st.write(f"- {a}")
