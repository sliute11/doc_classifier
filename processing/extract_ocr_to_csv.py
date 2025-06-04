# import os
# import csv
# from pathlib import Path
# from PIL import Image
# import pytesseract
# from tqdm import tqdm
# import sys
# import os
# import constants
# # --- Setup path for custom modules ---
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# from processing.file_reader import extract_text_from_file

# INPUT_DIR = constants.INPUT_DIR
# OUTPUT_CSV = constants.EXTRACTED_OCR
# pytesseract.pytesseract.tesseract_cmd = constants.TESSERACT_PATH
# data = []

# # Recursively search for .tif files
# tif_files = list(Path(INPUT_DIR).rglob("*.tif"))

# for tif_path in tqdm(tif_files, desc="Processing TIFFs"):
#     try:
#         # Use parent folder name as label
#         label = tif_path.parent.name
#         image = Image.open(tif_path).convert("RGB")
#         text = pytesseract.image_to_string(image)

#         if text.strip():  # skip empty OCR
#             data.append({"text": text.strip(), "label": label})
#         else:
#             print(f"⚠️ Empty OCR for: {tif_path}")
#     except Exception as e:
#         print(f"❌ Error processing {tif_path}: {e}")

# # Save to CSV
# with open(OUTPUT_CSV, "w", encoding="utf-8", newline="") as f:
#     writer = csv.DictWriter(f, fieldnames=["text", "label"])
#     writer.writeheader()
#     writer.writerows(data)

# print(f"✅ Done! Saved {len(data)} entries to {OUTPUT_CSV}")



# PARALLELLIZED VERSION

import os
import csv
import sys
from pathlib import Path
from PIL import Image
import pytesseract
from tqdm import tqdm
from multiprocessing import Pool
import constants

# Setup path for module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from processing.file_reader import extract_text_from_file

INPUT_DIR = constants.INPUT_DIR
OUTPUT_CSV = constants.EXTRACTED_OCR
pytesseract.pytesseract.tesseract_cmd = constants.TESSERACT_PATH

tif_files = list(Path(INPUT_DIR).rglob("*.tif"))

def process_file(tif_path):
    try:
        label = tif_path.parent.name
        image = Image.open(tif_path).convert("RGB")
        text = pytesseract.image_to_string(image)

        if text.strip():
            return {"text": text.strip(), "label": label}
        else:
            return "empty"
    except Exception as e:
        return f"error::{tif_path}::{e}"

if __name__ == "__main__":
    print(f"📁 Found {len(tif_files)} .tif files in '{INPUT_DIR}'")
    max_workers = constants.MAX_PARALLEL_WORKERS

    with Pool(processes=max_workers) as pool:
        results = list(tqdm(pool.imap(process_file, tif_files), total=len(tif_files), desc="🔍 Performing OCR"))

    final_data = []
    empty_count = 0
    error_count = 0
    error_paths = []

    for r in results:
        if isinstance(r, dict):
            final_data.append(r)
        elif r == "empty":
            empty_count += 1
        elif isinstance(r, str) and r.startswith("error::"):
            error_count += 1
            _, path, msg = r.split("::", 2)
            error_paths.append((path, msg))

    with open(OUTPUT_CSV, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["text", "label"])
        writer.writeheader()
        writer.writerows(final_data)

    print(f"\n✅ OCR completed!")
    print(f"🔢 Total files processed: {len(tif_files)}")
    print(f"🟢 Successful OCRs: {len(final_data)}")
    print(f"🟡 Empty OCRs: {empty_count}")
    print(f"🔴 Errors: {error_count}")

    if error_paths:
        print("\n🚫 Some files failed:")
        for path, msg in error_paths[:10]:  # show only first 10
            print(f"  - {path}: {msg}")
