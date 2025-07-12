import openai
from backend.retriever import LegalRetriever

# Load your OpenAI key
openai.api_key = "sk-..."  # Replace with your key or use environment variable

retriever = LegalRetriever()

def reason_with_gpt(case_facts: str):
    relevant_laws = retriever.search(case_facts)

    law_texts = "\n\n".join([f"{law['title']}:\n{law['text'][:500]}" for law in relevant_laws])
    
    prompt = f"""
You are a legal reasoning assistant. Given the case facts and relevant laws, provide a legal opinion.

Case Facts:
{case_facts}

Relevant Laws and Precedents:
{law_texts}

Answer in clear legal terms. Mention if the case facts satisfy any specific legal sections.
"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.4
    )

    return response['choices'][0]['message']['content']
