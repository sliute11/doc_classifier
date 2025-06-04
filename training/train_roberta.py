import torch
from torch.utils.data import Dataset, DataLoader
from torch.optim import AdamW
from transformers import RobertaTokenizer, RobertaForSequenceClassification
from sklearn.metrics import accuracy_score, classification_report
import pickle
import os
from tqdm import tqdm
import sys
import constants

# Setup module path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Load preprocessed data
with open(constants.TRAIN_TEXTS, "rb") as f:
    train_texts = pickle.load(f)
with open(constants.TRAIN_LABELS, "rb") as f:
    train_labels = pickle.load(f)
with open(constants.TEST_TEXTS, "rb") as f:
    test_texts = pickle.load(f)
with open(constants.TEST_LABELS, "rb") as f:
    test_labels = pickle.load(f)
with open(constants.LABEL_ENCODER, "rb") as f:
    label_encoder = pickle.load(f)

# Tokenize
print("🔤 Tokenizing texts...")
tokenizer = RobertaTokenizer.from_pretrained("roberta-base")
train_encodings = tokenizer(train_texts, truncation=True, padding=True, max_length=512)
test_encodings = tokenizer(test_texts, truncation=True, padding=True, max_length=512)

class DocDataset(Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels
    def __getitem__(self, idx):
        return {key: torch.tensor(val[idx]) for key, val in self.encodings.items()} | {"labels": torch.tensor(self.labels[idx])}
    def __len__(self):
        return len(self.labels)

train_dataset = DocDataset(train_encodings, train_labels)
test_dataset = DocDataset(test_encodings, test_labels)

# Model
num_labels = len(label_encoder.classes_)
model = RobertaForSequenceClassification.from_pretrained("roberta-base", num_labels=num_labels)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

if __name__ == "__main__":
    # AMP - Mixed precision
    use_fp16 = True
    scaler = torch.cuda.amp.GradScaler(enabled=use_fp16)

    # Dataloaders (GPU-friendly settings)
    train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True, num_workers=4, pin_memory=True)
    test_loader = DataLoader(test_dataset, batch_size=16, num_workers=2, pin_memory=True)

    # Optimizer
    optim = AdamW(model.parameters(), lr=5e-5)

    # Training loop
    print("🚀 Starting training...")
    model.train()
    for epoch in range(3):
        loop = tqdm(train_loader, desc=f"Epoch {epoch+1}")
        total_loss = 0
        for batch in loop:
            batch = {k: v.to(device) for k, v in batch.items()}
            optim.zero_grad()

            with torch.cuda.amp.autocast(enabled=use_fp16):
                outputs = model(**batch)
                loss = outputs.loss

            scaler.scale(loss).backward()
            scaler.step(optim)
            scaler.update()
            total_loss += loss.item()
            loop.set_postfix(loss=loss.item())

        print(f"🔁 Epoch {epoch+1} average loss: {total_loss / len(train_loader):.4f}")

    # Evaluation
    print("🔍 Starting evaluation...")
    model.eval()
    all_preds, all_labels = [], []
    with torch.no_grad():
        for batch in tqdm(test_loader, desc="Evaluating"):
            inputs = {k: v.to(device) for k, v in batch.items() if k != 'labels'}
            labels = batch["labels"].to(device)
            outputs = model(**inputs)
            preds = outputs.logits.argmax(dim=-1)
            all_preds.extend(preds.cpu().numpy())
            all_labels.extend(labels.cpu().numpy())

    acc = accuracy_score(all_labels, all_preds)
    print(f"\n✅ Accuracy: {acc:.4f}")
    print("📊 Classification Report:\n")
    print(classification_report(all_labels, all_preds, target_names=label_encoder.classes_))

    # Save model
    os.makedirs(constants.RETRAINED_MODEL, exist_ok=True)
    model.save_pretrained(constants.RETRAINED_MODEL)
    tokenizer.save_pretrained(constants.RETRAINED_MODEL)
    print(f"💾 Model saved to {constants.RETRAINED_MODEL}")
