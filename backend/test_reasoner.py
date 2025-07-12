from backend.reasoner import reason_with_gpt

case = """Ram Chandra Sharma was detained by police under suspicion without warrant or proper investigation. 
The detainment lasted over 72 hours without being presented to a magistrate."""

result = reason_with_gpt(case)
print("🧠 GPT Legal Reasoning:\n", result)
