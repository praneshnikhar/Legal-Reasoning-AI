import sys, os
sys.path.append(os.path.abspath(".."))

from backend.retriever import LegalRetriever

retriever = LegalRetriever()
query = "breach of contract with advance payment"
results = retriever.search(query)

for res in results:
    print(f"\n🔍 {res['title']}\n{res['text'][:400]}...\n")
