from transformers import pipeline


generator = pipeline("text-generation", model="distilgpt2")
prompt = "Welcome to the Keo AI. In this world,"
result = generator(prompt, max_length=50, num_return_sequences=1)

print(result[0]['generated_text'])