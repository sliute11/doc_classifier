import os
import time
import tracemalloc
from pathlib import Path
from multiprocessing import Pool
from PIL import Image
import pytesseract
import sys
import constants

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

INPUT_DIR = constants.INPUT_DIR
pytesseract.pytesseract.tesseract_cmd = constants.TESSERACT_PATH

# Use just 10 TIFFs to benchmark
tif_files = list(Path(INPUT_DIR).rglob("*.tif"))[:10]

def ocr_single(tif_path):
    try:
        image = Image.open(tif_path).convert("RGB")
        text = pytesseract.image_to_string(image)
        return bool(text.strip())  # Return True if non-empty OCR
    except Exception as e:
        print(f"Error: {e}")
        return False

def benchmark_pool(num_workers):
    print(f"\n⚙️  Testing with {num_workers} workers...")
    tracemalloc.start()
    start_time = time.time()

    with Pool(num_workers) as pool:
        results = pool.map(ocr_single, tif_files)

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"✅ OCR success rate: {sum(results)}/{len(results)}")
    print(f"⏱️  Time taken: {round(end_time - start_time, 2)} seconds")
    print(f"🧠 Peak memory usage: {round(peak / (1024 * 1024), 2)} MB")

if __name__ == "__main__":
    for workers in range(1, 13):  # Test 1 to 12 workers
        benchmark_pool(workers)
