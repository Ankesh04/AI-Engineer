import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key not found")

client = Groq(api_key = my_api_key)
model = "llama-3.3-70b-versatile"

def ask_llm(question):
    sys_prompt="answer in one line only"
    system_message={
        "role":"system",
        "content":sys_prompt
    }
    message={
        "role": "user",
        "content": question
    }
    messages=[system_message,message]
    response=client.chat.completions.create(model=model, messages=messages)
    answer=response.choices[0].message.content
    return answer

# question="do you know dazzido"
question="do know the age of dazzido"
print(ask_llm(question))
