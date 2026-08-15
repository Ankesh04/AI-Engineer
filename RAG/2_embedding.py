import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
import numpy as np
from sentence_transformers import SentenceTransformer

def cosine_similarity(a,b):
    return np.dot(a,b)/(
        np.linalg.norm(a) * np.linalg.norm(b)
    )

model= SentenceTransformer("all-MiniLM-L6-v2") #384
text = "Machine learning is fun."

# embedding = model.encode(text)
# print(embedding.shape)
# print(embedding[:10])
# output:[-0.00461604 -0.08052148  0.07581387  0.00348901 -0.04938735 -0.05615274
#  -0.06738347 -0.03651007 -0.01811039  0.04264413]

# t1="There are 24 paid leaves"
# t2="There are 24 vacation days"
# output:0.43657774

t1="There are 24 paid leaves"
t2="I love pizza"
# output:0.0573136

v1=model.encode(t1)
v2=model.encode(t2)
print(cosine_similarity(v1, v2))