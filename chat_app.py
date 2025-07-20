import gradio as gr
from transformers import pipeline

chatbot = pipeline("text-generation", model="distilgpt2")

def chat(prompt):   
    response = chatbot(prompt, max_length=50)[0]['generated_text']
    return response

gr.Interface(fn=chat, inputs="text", outputs="text", title="Mini LLM Chat").launch()