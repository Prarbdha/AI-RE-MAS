from agents.llm import llm

response = llm.invoke("Say hello and confirm you are Gemini.")
print(response.content)