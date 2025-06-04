import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pickle
import os
from tqdm import tqdm
import constants

# Input and output paths
RAW_PATH = constants.EXTRACTED_OCR_CLEANED  # <-- Add this to constants.py
PROCESSED_PATH = constants.PROCESSED_PATH   # already defined
os.makedirs(PROCESSED_PATH, exist_ok=True)

print("📦 Loading and cleaning data...")
df = pd.read_csv(RAW_PATH)[['text_cleaned', 'label']].dropna()
df = df.rename(columns={"text_cleaned": "text"})

print(f"🔢 Total samples: {len(df)}")

print("🔠 Encoding labels...")
label_encoder = LabelEncoder()
df['label_id'] = label_encoder.fit_transform(df['label'])

print("✂️ Splitting train/test data...")
train_texts, test_texts, train_labels, test_labels = train_test_split(
    df['text'].tolist(),
    df['label_id'].tolist(),
    test_size=0.2,
    random_state=42,
    stratify=df['label_id']
)

print("💾 Saving processed files...")
for name, obj in tqdm([
    ("train_texts.pkl", train_texts),
    ("test_texts.pkl", test_texts),
    ("train_labels.pkl", train_labels),
    ("test_labels.pkl", test_labels),
    ("label_encoder.pkl", label_encoder)
], desc="Saving", unit="file"):
    with open(os.path.join(PROCESSED_PATH, name), "wb") as f:
        pickle.dump(obj, f)

print("✅ Data preprocessing complete and saved.")
print(f"📂 Processed files saved to: {PROCESSED_PATH}")