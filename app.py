from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import gradio as gr
import pickle

tokenizer = AutoTokenizer.from_pretrained("saved_model")
model = AutoModelForSequenceClassification.from_pretrained("saved_model")
with open("label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

def predict(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
        pred = torch.argmax(outputs.logits, dim=1).item()
    return label_encoder.inverse_transform([pred])[0]

gr.Interface(fn=predict, inputs="text", outputs="text").launch()
