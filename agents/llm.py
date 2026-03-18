import os
import time
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.2,
)

def call_with_retry(chain, inputs, retries=3, delay=10):
    for attempt in range(retries):
        try:
            return chain.invoke(inputs)
        except Exception as e:
            if "429" in str(e) or "quota" in str(e).lower():
                print(f"Rate limit hit. Waiting {delay}s... (attempt {attempt+1})")
                time.sleep(delay)
            else:
                raise e
    raise Exception("Max retries exceeded.")