import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
import numpy as np
from sentence_transformers import SentenceTransformer


model= SentenceTransformer("all-MiniLM-L6-v2") #384

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key not found")

client = Groq(api_key = my_api_key)
groqmodel = "llama-3.3-70b-versatile"

# This is companies knowledge base
documents = [
    "Employees recieve 24 days of paid leave per year.",

    "Employees work from the office on tuesday, wednessday and thursday."
    "Monday and Friday are optional work-from-home days.",

    "Employees recieve Rs 3000 per month for gym reimbursement.",

    "Employees can claim Rs 2000 per month for home internet.",

    "Employees have a 90 day notice period."
]

document_embedding = model.encode(documents)
# every line converted to array

# here the document_embedding will consist of 7800+ charectors but it is very small content(knowledge base)
# but what if there are 100s of pdf then it must be of more that 1 cr charectors 
#to process this little data llm is taking 20 sec then what if 1 cr chrector would be take then it will take 6-7 hrs
# to conqure this vector db is used

def cosine_similarity(a,b):
    return np.dot(a,b)/(
        np.linalg.norm(a) * np.linalg.norm(b)
    )#to calculate score

def retrieve(q_embedding):
    scores = []

    for i, document in enumerate(document_embedding):
        score = cosine_similarity(q_embedding, document)
        scores.append((score, documents[i]))

    scores.sort(reverse=True)

    return scores[0]

def ask_llm(question,context):
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
    response=client.chat.completions.create(model=groqmodel, messages=messages)
    answer=response.choices[0].message.content
    return answer

query= "How much vacation do i get"
q_embedding=model.encode(query)
score,context=retrieve(q_embedding)
answer=ask_llm(query,context)
print(answer)