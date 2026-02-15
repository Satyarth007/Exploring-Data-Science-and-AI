from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = [
    "Dogs are allowed in the offices on fridays",
    "Pets can come to work on Fury Fridays",
    "Remote work policy allows 3 days work from home"
]

embeddings = model.encode(sentences)

sim_1_2 = np.dot(embeddings[0], embeddings[1])
sim_1_3 = np.dot(embeddings[0],embeddings[2])
sim_2_3 = np.dot(embeddings[1],embeddings[2])

print(f" Dogs vs Pets: {sim_1_2*100:.1f}% similar")
print(f" Dogs vs Remote: {sim_1_3*100:.1f}% similar")
print(f" Pets vs Remote: {sim_2_3*100:.1f}% similar")