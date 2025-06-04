import pandas as pd
import matplotlib.pyplot as plt

# Path to your cleaned dataset
CLEANED_CSV = r"E:\training\doc_classifier\data\Cleaned_OCR_Dataset.csv" 

# Load data
df = pd.read_csv(CLEANED_CSV)

# Count label occurrences
label_counts = df['label'].value_counts().sort_values(ascending=False)

# Plot
plt.figure(figsize=(12, 6))
label_counts.plot(kind='bar', color='skyblue')
plt.title("Document Type Distribution", fontsize=16)
plt.xlabel("Document Label", fontsize=12)
plt.ylabel("Number of Documents", fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show plot
plt.show()
