import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("API ERROR")

client = Groq(api_key = my_api_key)
model = "llama-3.3-70b-versatile"

#STRUCTURING THE LLMs OUTPUT SO THAT PROGRAMS ACCEPTING THE OUTPUT HAVE EASY TO DECIDE.
from pydantic import BaseModel
class Ticket(BaseModel):
    name:str
    email:str
    issue:str
schema = Ticket.model_json_schema()

response_format = {
    "type": "json_object"
}

system_prompt = f"""
Extract the personal information from the ticket strictly based on this schema and in json format.
{schema}
"""

message_system = {
    "role":"system",
    "content":system_prompt
}

role = "user"
text = "Hello my name is ankesh. I have an iphone which is not working at all. My address is bangalore. My email is abc@gmai.com. My contact number is 198393."
# the prompt will not be like this as this is an email.
# prompt = "Do you know Dazzido in youtube"
prompt = f"""
This is a customer ticket. Please extract the  personal information from this.
{text}
"""
message = {
    "role" : role,
    "content" : prompt
}
messages = [message_system, message]

response = client.chat.completions.create(model = model, messages = messages, response_format = response_format)

answer = response.choices[0].message.content
print(answer)


# how the developer will read this 
import json
raw_json=answer
data_file = json.loads(raw_json)
ticket = Ticket(**data_file)

print(ticket.name)
print(ticket.email)
print(ticket.issue)