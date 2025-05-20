import os
import csv
from pathlib import Path
from PIL import Image
import pytesseract
from tqdm import tqdm
import sys
import os
import constants
# --- Setup path for custom modules ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from processing.file_reader import extract_text_from_file

INPUT_DIR = constants.INPUT_DIR
OUTPUT_CSV = constants.EXTRACTED_OCR
pytesseract.pytesseract.tesseract_cmd = constants.TESSERACT_PATH
data = []

# Recursively search for .tif files
tif_files = list(Path(INPUT_DIR).rglob("*.tif"))

for tif_path in tqdm(tif_files, desc="Processing TIFFs"):
    try:
        # Use parent folder name as label
        label = tif_path.parent.name
        image = Image.open(tif_path).convert("RGB")
        text = pytesseract.image_to_string(image)

        if text.strip():  # skip empty OCR
            data.append({"text": text.strip(), "label": label})
        else:
            print(f"⚠️ Empty OCR for: {tif_path}")
    except Exception as e:
        print(f"❌ Error processing {tif_path}: {e}")

# Save to CSV
with open(OUTPUT_CSV, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["text", "label"])
    writer.writeheader()
    writer.writerows(data)

print(f"✅ Done! Saved {len(data)} entries to {OUTPUT_CSV}")
