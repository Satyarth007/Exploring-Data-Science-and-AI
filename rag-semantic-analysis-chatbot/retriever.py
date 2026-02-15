from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("knowledge.txt") as f:
    docs = [l.strip() for l in f.readlines()]

embeddings = model.encode(docs)

def retrieve(query):
    q = model.encode([query])[0]
    scores = np.dot(embeddings, q)
    return docs[np.argmax(scores)]
