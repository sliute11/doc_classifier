import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pickle
import os
from tqdm import tqdm

# Paths
RAW_PATH = r"C:\Users\lfratila\OneDrive - ENDAVA\Projects\Document-Classifier\doc_classifier\data\outputs-sampled.csv"
PROCESSED_PATH = r"C:\Users\lfratila\OneDrive - ENDAVA\Projects\Document-Classifier\doc_classifier\data\processed"
os.makedirs(PROCESSED_PATH, exist_ok=True)

# Load and clean
print("📦 Loading and cleaning data...")
df = pd.read_csv(RAW_PATH)[['text', 'label']].dropna()

print(f"🔢 Total samples: {len(df)}")

label_encoder = LabelEncoder()
df['label_id'] = label_encoder.fit_transform(df['label'])

# Split
print("✂️ Splitting train/test data...")
train_texts, test_texts, train_labels, test_labels = train_test_split(
    df['text'].tolist(),
    df['label_id'].tolist(),
    test_size=0.2,
    random_state=42,
    stratify=df['label_id']
)

# Save splits and label encoder with tqdm
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
