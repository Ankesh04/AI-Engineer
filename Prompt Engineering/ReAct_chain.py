import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("API Not Found!")

client = Groq(api_key = my_api_key)
model = "llama-3.3-70b-versatile"

# Tools
# General tool without api just functions
def get_product_price(product):
    if product == 'iPhone 17':
        return 1000
    elif product == 'iPhone 15':
        return 500
    else:
        return 0
    
