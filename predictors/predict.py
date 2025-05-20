import pandas as pd
import torch
from torch.utils.data import Dataset, DataLoader
from transformers import RobertaTokenizer, RobertaForSequenceClassification
from sklearn.metrics import accuracy_score, classification_report
import pickle
import os
import constants

# ==== CONFIG ====
INPUT_CSV = constants.INPUT_CSV
OUTPUT_CSV = constants.OUTPUT_CSV
MODEL_PATH = constants.MODEL_PATH
ENCODER_PATH = constants.ENCODER_PATH

BATCH_SIZE = 8
MAX_LEN = 512

# ==== Load Input ====
df = pd.read_csv(INPUT_CSV)
has_labels = "label" in df.columns

texts = df["text"].dropna().tolist()
true_labels = df["label"].tolist() if has_labels else None

# ==== Load Model and Tokenizer ====
model = RobertaForSequenceClassification.from_pretrained(MODEL_PATH)
tokenizer = RobertaTokenizer.from_pretrained(MODEL_PATH)
with open(ENCODER_PATH, "rb") as f:
    label_encoder = pickle.load(f)

# ==== Encode ====
encodings = tokenizer(texts, truncation=True, padding=True, max_length=MAX_LEN)

# ==== Dataset ====
class InferenceDataset(Dataset):
    def __init__(self, encodings):
        self.encodings = encodings
    def __getitem__(self, idx):
        return {k: torch.tensor(v[idx]) for k, v in self.encodings.items()}
    def __len__(self):
        return len(self.encodings["input_ids"])

dataset = InferenceDataset(encodings)
loader = DataLoader(dataset, batch_size=BATCH_SIZE)

# ==== Inference ====
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()

preds = []
with torch.no_grad():
    for batch in loader:
        batch = {k: v.to(device) for k, v in batch.items()}
        outputs = model(**batch)
        predicted = torch.argmax(outputs.logits, dim=1)
        preds.extend(predicted.cpu().numpy())

decoded_preds = label_encoder.inverse_transform(preds)
df["predicted_label"] = decoded_preds

# ==== Accuracy Metrics (Optional) ====
if has_labels:
    true_encoded = label_encoder.transform(true_labels)
    acc = accuracy_score(true_encoded, preds)
    print(f"✅ Test Accuracy: {acc:.4f}")
    
    print("📊 Classification Report:")
    print(classification_report(true_encoded, preds, target_names=label_encoder.classes_))

# ==== Save Predictions ====
os.makedirs(os.path.dirname(OUTPUT_CSV), exist_ok=True)
df.to_csv(OUTPUT_CSV, index=False)
print(f"✅ Predictions saved to: {OUTPUT_CSV}")
