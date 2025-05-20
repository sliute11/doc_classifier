import os
from pathlib import Path
from PIL import Image
import pytesseract
import sys
import os
import constants
# --- Setup path for custom modules ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

pytesseract.pytesseract.tesseract_cmd = constants.TESSERACT_PATH

try:
    import pdfplumber
except ImportError:
    pdfplumber = None

try:
    import docx
except ImportError:
    raise ImportError("python-docx not installed. Please install it with 'pip install python-docx'.")

def extract_text_from_pdf(file_path):
    if not pdfplumber:
        raise ImportError("pdfplumber is not installed. Install it with 'pip install pdfplumber'.")

    text = ""
    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
                else:
                # OCR fallback
                    image = page.to_image(resolution=300).original.convert("RGB")
                    text += pytesseract.image_to_string(image) + "\n"
    except Exception as e:
        raise RuntimeError(f"PDF extraction failed for {file_path}: {e}")

    if not text.strip():
        raise ValueError(f"⚠️ No extractable text found in PDF: {file_path}")
    
    return text.strip()

def extract_text_from_docx(file_path):
    try:
        doc = docx.Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs]).strip()
    except Exception as e:
        raise RuntimeError(f"DOCX extraction failed for {file_path}: {e}")

def extract_text_from_txt(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read().strip()
    except Exception as e:
        raise RuntimeError(f"TXT extraction failed for {file_path}: {e}")
    
def extract_text_from_image(file_path):
    image = Image.open(file_path)
    return pytesseract.image_to_string(image)

def extract_text_from_file(file_path):
    ext = Path(file_path).suffix.lower()
    if ext == '.pdf':
        return extract_text_from_pdf(file_path)
    elif ext == '.docx':
        return extract_text_from_docx(file_path)
    elif ext == '.txt':
        return extract_text_from_txt(file_path)
    elif ext in [".png", ".jpg", ".jpeg", ".tiff",".tif"]:
        return extract_text_from_image(file_path)
    else:
        raise ValueError(f"❌ Unsupported file type: {ext}")
