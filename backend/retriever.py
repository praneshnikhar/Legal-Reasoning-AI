import os
import json
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

class LegalRetriever:
    def __init__(self, data_folder="data"):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.texts = []
        self.titles = []
        self.load_data(data_folder)
        self.create_index()

    def load_data(self, folder):
        for filename in os.listdir(folder):
            if filename.endswith(".json"):
                with open(os.path.join(folder, filename), "r") as f:
                    data = json.load(f)
                    self.titles.append(data["title"])
                    self.texts.append(data["text"])

    def create_index(self):
        self.embeddings = self.model.encode(self.texts, show_progress_bar=True)
        self.index = faiss.IndexFlatL2(len(self.embeddings[0]))
        self.index.add(np.array(self.embeddings))

    def search(self, query, k=3):
        query_embedding = self.model.encode([query])
        distances, indices = self.index.search(np.array(query_embedding), k)
        results = []
        for idx in indices[0]:
            results.append({
                "title": self.titles[idx],
                "text": self.texts[idx]
            })
        return results
