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

def llm_ans(prompt):
    message = {
        "role" : "user",
        "content" : prompt
    }
    messages = [message]
    response = client.chat.completions.create(model=model, messages=messages)
    ans = response.choices[0].message.content
    return ans

bad_prompt= """
This is a user complaint:
My laptop is not working.
Classify this
"""
# print(llm_ans(bad_prompt))
# I would classify this as a:
# **Technical Support Issue**
# More specifically, it's a **Hardware Issue**, as the user is reporting a problem with their laptop, which is a physical device.

role_prompt= """
#Role:
You are a support assistant at a mobile/laptop company
This is a user complaint:
My laptop is not working.
Classify this
"""
# print(llm_ans(role_prompt))
# I would classify this complaint as a:
# **Hardware Issue**
# Specifically, it falls under the category of:
# **General Fault/Not Turning On**
# As the user has reported that their laptop is "not working", which suggests a potential problem with the device's functionality, but doesn't provide any specific symptoms or error messages. I would need to ask follow-up questions to gather more information and troubleshoot the issue.

task_prompt= """
#Role:
You are a support assistant at a mobile/laptop company
#Task
You have to classify the issue in a category
This is a user complaint:
My laptop is not working.
"""
# print(llm_ans(task_prompt))
# I'd be happy to help you with that issue. Based on your complaint, "My laptop is not working," I would classify this issue under the category of:
# **Hardware/ Startup Issues**
# This category includes problems related to the laptop's ability to power on, boot up, or function properly. I'd be happy to help you troubleshoot or provide further assistance to resolve the issue. Can you please provide more details about the problem you're experiencing?

constraint_prompt= """
#Role:
You are a support assistant at a mobile/laptop company
#Task
You have to classify the issue in a category
#CONSTRAINT
You have to classify the issue in one of the three category namely billing, technical or return
This is a user complaint:
My laptop is not working.
"""
# print(llm_ans(constraint_prompt))
# Based on the user's complaint, "My laptop is not working", I would classify the issue in the category of **Technical**. The user is experiencing a problem with the functionality of their laptop, which suggests a technical issue rather than a billing or return-related problem.
constraint2_prompt= """
#Role:
You are a support assistant at a mobile/laptop company
#Task
You have to classify the issue in a category
#CONSTRAINT
You have to classify the issue in one of the three category namely billing, technical , return
This is a user complaint:
My girlfriend left me.
"""
# print(llm_ans(constraint2_prompt))
# I'm so sorry to hear that you're going through a tough time. However, I have to classify your issue into one of the three categories: billing, technical, or return. Since your issue is related to a personal matter and not directly related to our mobile/laptop products or services, I would say that it doesn't fit into any of the three categories. But if I had to choose, I would say that it's not applicable to any of the categories, as it's a personal issue.
# To be more specific, I would say that it's "Not Applicable" to our support categories, but since that's not an option, I would choose "None of the above" if that was an option. However, since I have to choose one of the three, I would say "Return" is the least related, but please note that this is not a correct classification, as your issue is not related to our products or services.
# Please let me know if there's anything else I can help you with, or if you'd like to talk about something else.

output_format_prompt= """
#Role:
You are a support assistant at a mobile/laptop company.
#Task
You have to classify the issue in a category.
#CONSTRAINT
You have to classify the issue in one of the three category namely billing, technical or return.
#OOTPUT FORMAT
Your answer should be in one word only. The one word should be one of the categories given in constraints.
This is a user complaint:
My laptop is not working.
"""
# print(llm_ans(output_format_prompt))
# Technical
output_format2_prompt= """
#ROLE
You are a support assistant at a mobile/laptop company.
#TASK
You have to classify the issue in a category.
#CONSTRAINT
You have to classify the issue in one of the three category namely billing, technical or return.
#OUTPUT FORMAT
Your answer should be in one word only. The one word should be one of the categories given in constraints.
This is a user complaint:
my girlfriend left me
"""
# print(llm_ans(output_format2_prompt))
# Technical

one_shot_prompt= """
#ROLE
You are a support assistant at a mobile/laptop company.
#TASK
You have to classify the issue in a category.
#CONSTRAINT
You have to classify the issue in one of the three category namely billing, technical or return.
#OUTPUT FORMAT
Your answer should be in one word only. The one word should be one of the categories given in constraints.
#EXAMPLE
For instance if a user complain says he wants a refund then the category is return
This is a user complaint:
my laptop is not working
"""
# print(llm_ans(one_shot_prompt))
# Technical
one_shot2_prompt= """
#ROLE
You are a support assistant at a mobile/laptop company.
#TASK
You have to classify the issue in a category.
#CONSTRAINT
You have to classify the issue in one of the three category namely billing, technical or return.
#OUTPUT FORMAT
Your answer should be in one word only. The one word should be one of the categories given in constraints.
#EXAMPLE
For instance if a user complain says he wants a refund then the category is return
This is a user complaint:
my girlfriend left me
"""
# print(llm_ans(one_shot2_prompt))
# Technical

fall_back_prompt= """
#ROLE
You are a support assistant at a mobile/laptop company.
#TASK
You have to classify the issue in a category.
#CONSTRAINT
You have to classify the issue in one of the three category namely billing, technical or return.
#OUTPUT FORMAT
Your answer should be in one word only. The one word should be one of the categories given in constraints.
#EXAMPLE
For instance if a user complain says he wants a refund then the category is return
#FALLBACK
If the issue is unrelated to any of the categories mentioned in constraints, then the answer should be OTHER
This is a user complaint:
my girlfriend left me
"""
print(llm_ans(fall_back_prompt))
# OTHER
# this was the production ready prompt example