import pandas as pd
import os
import sys

import constants
# --- Setup path for custom modules ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Load the original data
df = pd.read_csv(constants.FULL_PROCESSED_DATASET)

# Drop NAs just to be sure
df = df[['text', 'label']].dropna()

# Sample 100 rows per label
sampled_df = df.groupby("label").apply(lambda x: x.sample(n=200, random_state=42)).reset_index(drop=True)

# Shuffle the full set (optional but useful)
sampled_df = sampled_df.sample(frac=1, random_state=42).reset_index(drop=True)

# Preview
print(sampled_df['label'].value_counts())
print(sampled_df.head())
sampled_df.to_csv(constants.SAMPLE_DATASET, index=False)
