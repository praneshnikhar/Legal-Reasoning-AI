import streamlit as st
from backend.retriever import LegalRetriever
from backend.reasoner import reason_with_gpt

st.set_page_config(page_title="LexAI - Legal Reasoning AI", layout="wide")

st.title("⚖️ LexAI – Legal Reasoning Assistant")
st.markdown("Enter a legal case summary or situation below. LexAI will retrieve relevant laws and reason over the case using GPT.")

with st.form("case_form"):
    case_input = st.text_area("📝 Enter Case Description", height=200, placeholder="e.g., The police detained a man for over 72 hours without a warrant...")
    submitted = st.form_submit_button("Analyze Case")

if submitted:
    if case_input.strip() == "":
        st.warning("Please enter a case summary.")
    else:
        with st.spinner("🔍 Retrieving relevant laws..."):
            retriever = LegalRetriever()
            laws = retriever.search(case_input)
        
        st.subheader("📚 Relevant Legal Sections")
        for i, law in enumerate(laws):
            with st.expander(f"{law['title']}"):
                st.write(law["text"][:1000] + "..." if len(law["text"]) > 1000 else law["text"])

        with st.spinner("🧠 Reasoning with GPT..."):
            reasoning = reason_with_gpt(case_input)

        st.subheader("🧠 LexAI's Legal Reasoning")
        st.markdown(reasoning)
