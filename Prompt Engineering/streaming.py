import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")

client=Groq(api_key=my_api_key)
model="llama-3.3-70b-versatile"

prompt = "Ëxplain how internet works."
message = {
    "role": "user",
    "content": prompt
}
messages = [message]

# NORMAL REPONSE STREAM = FALSE
# response1= client.chat.completions.create(model=model, messages=messages)
# answer = response1.choices[0].message.content
# print(answer)
# here reponse tooks time to display but dislayed all at once

stream = client.chat.completions.create(model=model, messages=messages, stream = True)
# in this stream many chunks will be created so we have to display it in other way
for chunk in stream:
    content = chunk.choices[0].delta.content
    if content:
        print(content, end = "", flush=True)
