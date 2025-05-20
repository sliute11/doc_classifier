import sys
import os
import pickle
import torch
from transformers import RobertaTokenizer, RobertaForSequenceClassification
# --- Setup path for custom modules ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from processing.file_reader import extract_text_from_file
import constants



# --- Configuration ---
MODEL_PATH = constants.MODEL_PATH
LABEL_ENCODER_PATH = constants.LABEL_ENCODER_PATH
FILES_DIR = constants.FILES_DIR

SUPPORTED_EXTENSIONS = constants.SUPPORTED_EXTENSIONS

# --- Load model and tokenizer ---
model = RobertaForSequenceClassification.from_pretrained(MODEL_PATH)
tokenizer = RobertaTokenizer.from_pretrained(MODEL_PATH)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()

# --- Load label encoder ---
with open(LABEL_ENCODER_PATH, "rb") as f:
    label_encoder = pickle.load(f)

# --- Collect valid file paths ---
file_paths = [
    os.path.join(FILES_DIR, fname)
    for fname in os.listdir(FILES_DIR)
    if os.path.splitext(fname)[1].lower() in SUPPORTED_EXTENSIONS
]

if not file_paths:
    print("⚠️ No supported documents found in the directory.")
    sys.exit(1)

# --- Extract text from each file ---
texts = []
valid_files = []
for file_path in file_paths:
    try:
        text = extract_text_from_file(file_path)
        if text.strip():
            texts.append(text)
            valid_files.append(file_path)
        else:
            print(f"⚠️ Skipped empty/unreadable: {file_path}")
    except Exception as e:
        print(f"❌ Error reading {file_path}: {e}")

if not texts:
    print("⚠️ No valid documents with extractable text.")
    sys.exit(1)

# --- Batch prediction ---
inputs = tokenizer(texts, truncation=True, padding=True, max_length=512, return_tensors="pt").to(device)
with torch.no_grad():
    logits = model(**inputs).logits
    probs = torch.nn.functional.softmax(logits, dim=1)
    preds = torch.argmax(probs, dim=1).cpu().tolist()
    confidences = probs.max(dim=1).values.cpu().tolist()

labels = label_encoder.inverse_transform(preds)

# --- Output results ---
print("\n📄 Prediction Results:")
for file_path, label, confidence in zip(valid_files, labels, confidences):
    print(f"→ {os.path.basename(file_path)} ➜ {label} ({confidence:.2%} confidence)")
