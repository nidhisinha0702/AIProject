import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2") #784
text = "Machine learning is fun"

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

#embedding=model.encode(text)
#print(embedding.shape)
#print(embedding[ :10])

t1 = "There are 24 paid leaves"
t2 = "There are 24 vacation days"

v1 = model.encode(t1)
v2 = model.encode(t2)
print(cosine_similarity(v1, v2))