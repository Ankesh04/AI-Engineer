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

# RAG 1st ITERRATION

#step1
# make knowledge base
knowledge_base={
    "age": "The age of dazzido is 22",
    "net worth": "the net worth of dazzido is 100000"
}

# step2
# retrive software
def retrive_info(question):
    question=question.lower()
    if "age" in question:
        return knowledge_base
    elif "net worth" in question:
        return knowledge_base
    else:
        return None

def ask_llm(question):
    context=retrive_info(question)
    sys_prompt=f"""Answer in one line only. Answer only based on this context, do not halucinate. Context: {context}"""
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
# question="do know the age of dazzido"  answer is available
question="do know the how old is dazzido"  #asnwer is not available as for the software old is not equal to age


print(ask_llm(question))

