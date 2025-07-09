from processing.file_reader import extract_text_from_file
import torch
from transformers import RobertaTokenizer, RobertaForSequenceClassification
import pickle
import os
import constants

MODEL_PATH = constants.MODEL_PATH
ENCODER_PATH = constants.LABEL_ENCODER

# --- Load model and tokenizer ---
print("[DEBUG] Loading model from:", MODEL_PATH)
try:
    print("[DEBUG] Files in model folder:", os.listdir(MODEL_PATH))
except Exception as e:
    print("[ERROR] Could not list files in model path:", e)

try:
    model = RobertaForSequenceClassification.from_pretrained(MODEL_PATH)
    tokenizer = RobertaTokenizer.from_pretrained(MODEL_PATH)
    print("[DEBUG] Model and tokenizer loaded successfully.")
except Exception as e:
    print("[ERROR] Failed to load HuggingFace model/tokenizer:", e)
    model = None
    tokenizer = None

# --- Load label encoder ---
try:
    with open(ENCODER_PATH, "rb") as f:
        label_encoder = pickle.load(f)
    print("[DEBUG] Label encoder loaded.")
except Exception as e:
    print("[ERROR] Failed to load label encoder:", e)
    label_encoder = None

# --- Set device ---
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
if model:
    model.to(device)
    model.eval()

# --- Prediction Function ---
def predict_document_type(file_path):
    if model is None or tokenizer is None or label_encoder is None:
        return "model_error", 0.0

    try:
        text = extract_text_from_file(file_path)
        if not text.strip():
            raise ValueError("No extractable text found in the file.")

        inputs = tokenizer(
            text,
            truncation=True,
            padding=True,
            max_length=512,
            return_tensors="pt"
        ).to(device)

        with torch.no_grad():
            logits = model(**inputs).logits
            probs = torch.nn.functional.softmax(logits, dim=1)
            pred_id = torch.argmax(probs, dim=1).item()
            confidence = probs[0][pred_id].item()
        
        label = label_encoder.inverse_transform([pred_id])[0]
        print(f"[DEBUG] Predicted label: {label}, confidence: {confidence:.2f}")
        return label, confidence

    except Exception as e:
        print("[ERROR] Prediction failed:", e)
        return "prediction_error", 0.0
