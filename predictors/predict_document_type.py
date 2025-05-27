from processing.file_reader import extract_text_from_file
import torch
from transformers import RobertaTokenizer, RobertaForSequenceClassification
import pickle
import os

MODEL_PATH = r"C:\Users\sliute\OneDrive - ENDAVA\doc_classifier_extra\models\roberta_model"
ENCODER_PATH = r"C:\Users\sliute\OneDrive - ENDAVA\doc_classifier_extra\models\label_encoder.pkl"

# Load once
model = RobertaForSequenceClassification.from_pretrained(MODEL_PATH)
tokenizer = RobertaTokenizer.from_pretrained(MODEL_PATH)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()

with open(ENCODER_PATH, "rb") as f:
    label_encoder = pickle.load(f)

def predict_document_type(file_path):
    text = extract_text_from_file(file_path)
    if not text.strip():
        raise ValueError("No extractable text found in the file.")
    
    inputs = tokenizer(text, truncation=True, padding=True, max_length=512, return_tensors="pt").to(device)
    with torch.no_grad():
        logits = model(**inputs).logits
        probs = torch.nn.functional.softmax(logits, dim=1)
        pred_id = torch.argmax(probs, dim=1).item()
        confidence = probs[0][pred_id].item()
    label = label_encoder.inverse_transform([pred_id])[0]
    return label, confidence
