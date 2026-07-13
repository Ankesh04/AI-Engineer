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

#***SYSTEM ROLE***
# role = "user"
# prompt = "I love you"

# message_system = {
#     "role" : "system",
#     # "content" : "You are my loving girlfriend"        
#     "content" : "You are my strict office collegue whi is also my manager" #post change
# }

role = "user"
prompt = "Suggest a name for my food company"

message_system = {
    "role" : "system",     
    "content" : "You are A BRAND MANAGER who suggest name for my food company. Name should be in one word." 
}

message = {
    "role" : role,
    "content" : prompt
}
messages = [message_system, message]
# Temperature by default is 0 meaning safe.
response = client.chat.completions.create(model = model, messages = messages, temperature=2)
# print(response)

print("#########################################/n")

answer = response.choices[0].message.content
print(answer)