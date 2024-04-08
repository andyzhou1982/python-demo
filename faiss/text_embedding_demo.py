import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('moka-ai/m3e-base')
sentences = [
    '这是一本介绍烹饪的书籍',
    '这是一本介绍运动的书籍',
    '篮球技术指南',
    '改装车操作手册',
    '鱼香肉丝的做法',
]
embeddings = model.encode(sentences)
'''
for sentence, embedding in zip(sentences, embeddings):
    print("Sentence:", sentence)
    print("Embedding:", embedding)
    print("")
'''
index = faiss.IndexFlatL2(len(embeddings[0]))
print(index.is_trained)
index.add(embeddings)
print(index.ntotal)

xq = model.encode(['如何成为一名厨师'])
k = 4                   # topK的K值
D, I = index.search(xq, k)# xq为待检索向量，返回的I为每个待检索query最相似TopK的索引list，D为其对应的距离
score = D[0][0]
similar_id = int(I[0][0])
print(score)
print(similar_id)
similar_embedding = embeddings[similar_id]
similar_sentence = sentences[similar_id]
#print("Embedding for ID", id, ":", similar_embedding)
print("Sentence for ID", id, ":", similar_sentence)

