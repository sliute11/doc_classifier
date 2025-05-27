# Path to the model and label encoder
MODEL_PATH = r"C:\Users\sliute\OneDrive - ENDAVA\doc_classifier_extra\models\roberta_model"
LABEL_ENCODER_PATH = r"C:\Users\sliute\OneDrive - ENDAVA\doc_classifier_extra\models\label_encoder.pkl"
FILES_DIR = r"C:\Users\sliute\OneDrive - ENDAVA\doc_classifier_extra\data\images"  # Folder with files

# Processing paths
INPUT_CSV = r"C:\Users\sliute\OneDrive - ENDAVA\doc_classifier_extra\data\company-document-text-sampled.csv"
OUTPUT_CSV = r"C:\Users\sliute\OneDrive - ENDAVA\doc_classifier_extra\data\predictions.csv"

ENCODER_PATH = r"C:\Users\sliute\OneDrive - ENDAVA\doc_classifier_extra\models\label_encoder.pkl"

RAW_PATH = r"C:\Users\sliute\OneDrive - ENDAVA\doc_classifier_extra\data\outputs-sampled.csv"
PROCESSED_PATH = r"C:\Users\sliute\OneDrive - ENDAVA\doc_classifier_extra\data\processed"

# File formats
SUPPORTED_EXTENSIONS = [".pdf", ".docx", ".txt", ".png", ".jpg", ".jpeg", ".tif", ".tiff"]

# Path to the full processed dataset
FULL_PROCESSED_DATASET = r"C:\Users\sliute\OneDrive - ENDAVA\doc_classifier_extra\data\outputs.csv"
# Path to sample dataset
SAMPLE_DATASET = r"C:\Users\sliute\OneDrive - ENDAVA\doc_classifier_extra\data\outputs-sampled.csv"

# Path to images directory
INPUT_DIR = r"C:\Users\sliute\OneDrive - ENDAVA\doc_classifier_extra\data\images"
# Output for CSV with full OCR
EXTRACTED_OCR = r"C:\Users\sliute\OneDrive - ENDAVA\doc_classifier_extra\data\outputs.csv"

# Path to Tesseract executable (adjust if needed)
TESSERACT_PATH = r"C:\Endava\EnDevLocal\Tesseract\tesseract.exe"

# Paths required for training
TRAIN_TEXTS = r"C:\Users\sliute\OneDrive - ENDAVA\doc_classifier_extra\models\train_texts.pkl"
TRAIN_LABELS = r"C:\Users\sliute\OneDrive - ENDAVA\doc_classifier_extra\models\train_labels.pkl"
TEST_TEXTS = r"C:\Users\sliute\OneDrive - ENDAVA\doc_classifier_extra\models\test_texts.pkl"
TEST_LABELS = r"C:\Users\sliute\OneDrive - ENDAVA\doc_classifier_extra\models\test_labels.pkl"
LABEL_ENCODER = r"C:\Users\sliute\OneDrive - ENDAVA\doc_classifier_extra\models\label_encoder.pkl"

# Path to the retrained model
RETRAINED_MODEL = r"C:\Users\sliute\OneDrive - ENDAVA\doc_classifier_extra\models\retrained_model"