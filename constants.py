


#Path to the model and label encoder
MODEL_PATH = r"C:\Users\lfratila\OneDrive - ENDAVA\Projects\Document-Classifier\doc_classifier\models\roberta_model"
LABEL_ENCODER_PATH = r"C:\Users\lfratila\OneDrive - ENDAVA\Projects\Document-Classifier\doc_classifier\models\label_encoder.pkl"
FILES_DIR = r"C:\Users\lfratila\OneDrive - ENDAVA\Projects\Document-Classifier\doc_classifier\data\images"  # folder with files


#Processing paths
# Path to the CSV file containing the text data
INPUT_CSV = r"C:\Users\lfratila\OneDrive - ENDAVA\Projects\Document-Classifier\company-document-text-sampled.csv"
OUTPUT_CSV = r"C:\Users\lfratila\OneDrive - ENDAVA\Projects\Document-Classifier\predictions.csv"

ENCODER_PATH = r"C:\Users\lfratila\OneDrive - ENDAVA\Projects\Document-Classifier\doc_classifier\data\processed\label_encoder.pkl"

#
RAW_PATH = r"C:\Users\lfratila\OneDrive - ENDAVA\Projects\Document-Classifier\doc_classifier\data\outputs-sampled.csv"
PROCESSED_PATH = r"C:\Users\lfratila\OneDrive - ENDAVA\Projects\Document-Classifier\doc_classifier\data\processed"

# File formats
SUPPORTED_EXTENSIONS = [".pdf", ".docx", ".txt", ".png", ".jpg", ".jpeg", ".tif",".tiff"]

# Path tp the full processed dataset
FULL_PROCESSED_DATASET = r"C:\Users\lfratila\OneDrive - ENDAVA\Projects\Document-Classifier\doc_classifier\data\outputs.csv"
# Path to sample dataset
SAMPLE_DATASET = r"C:\Users\lfratila\OneDrive - ENDAVA\Projects\Document-Classifier\doc_classifier\data\outputs-sampled.csv"

# Path to images directory
INPUT_DIR = r"C:\Learning\dataset_project\test"
# Output for CSV with full OCR
EXTRACTED_OCR = r"C:\Users\lfratila\OneDrive - ENDAVA\Projects\Document-Classifier\doc_classifier\data\outputs.csv"

# Path to Tesseract executable
TESSERACT_PATH = r'C:\sseract\tesseract.exe'

# Paths required for training
TRAIN_TEXTS = r"C:\Users\lfratila\OneDrive - ENDAVA\Projects\Document-Classifier\doc_classifier\models\train_texts.pkl"
TRAIN_LABELS = r"C:\Users\lfratila\OneDrive - ENDAVA\Projects\Document-Classifier\doc_classifier\models\train_labels.pkl"
TEST_TEXTS = r"C:\Users\lfratila\OneDrive - ENDAVA\Projects\Document-Classifier\doc_classifier\models\test_texts.pkl"
TEST_LABELS = r"C:\Users\lfratila\OneDrive - ENDAVA\Projects\Document-Classifier\doc_classifier\models\test_labels.pkl"
LABEL_ENCODER = r"C:\Users\lfratila\OneDrive - ENDAVA\Projects\Document-Classifier\doc_classifier\models\label_encoder.pkl"

#Path to the retrained model
RETRAINED_MODEL = r"C:\Users\lfratila\OneDrive - ENDAVA\Projects\Document-Classifier\doc_classifier\models\retrained_model"