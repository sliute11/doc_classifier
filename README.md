# 🧾 Document Classifier

A machine learning pipeline that uses OCR and a RoBERTa-based model to classify documents such as invoices, resumes, and more.

---

## 🚀 Features

- Upload PDFs or images via a web interface
- Extract OCR text using custom preprocessing
- Classify document type using a trained RoBERTa model
- Built with FastAPI (backend) and React + Tailwind (frontend)
- Optimized for local development (no Docker required)

---

## 📂 Project Structure

```bash
.
├── api/                    # FastAPI backend with app.py
├── predictors/             # Model prediction logic
├── processing/             # OCR and data extraction
├── training/               # Preprocessing and model training
├── visualization/          # Data and model analysis scripts
├── frontend/               # React + Vite UI
├── models/                 # HuggingFace model + label encoder
├── Dockerfile              # Backend Dockerfile
├── docker-compose.yml      # Compose for full stack
├── requirements.txt        # Python dependencies
├── docs/                   # Dev setup instructions
├── CONTRIBUTE.md           # Team roles and issue assignments
└── README.md               # This file
```

---

## 🗂 Dataset Reference: RVL-CDIP

This project leverages a subset of the RVL-CDIP dataset, a benchmark document classification corpus originally compiled by the Ryerson Vision Lab. It contains over 400,000 grayscale document images categorized into 16 classes, including:

- Invoice, Resume, Letter, Memo, Email, Questionnaire
- Scientific Report, Budget, News Article, Presentation, and more

For **model evaluation and testing, we use the RVL-CDIP test subset**, which provides **pre-labeled documents** to validate classification accuracy. The dataset supports robust training and evaluation of multi-class document classification models, such as the RoBERTa-based classifier implemented in this pipeline.

## 🧠 Pipeline Overview

### 1. Data Preparation

- **OCR Extraction:**  
  Raw documents (PDFs, TIFFs, images) are processed using Tesseract OCR to extract their text content.  
  See [`processing/extract_ocr_to_csv.py`](processing/extract_ocr_to_csv.py) and [`processing/file_reader.py`](processing/file_reader.py).
- **Label Assignment:**  
  Each document is assigned a label (e.g., "invoice", "form", "presentation") based on its folder or metadata.
- **CSV Creation:**  
  The extracted text and labels are saved into a CSV file, with columns like `text` and `label`.

### 2. Preprocessing

- **Cleaning:**  
  The text is cleaned (removing noise, fixing OCR errors, etc.).
- **Label Encoding:**  
  Labels are converted to numeric IDs using scikit-learn’s `LabelEncoder`.
- **Train/Test Split:**  
  The dataset is split into training and test sets (typically 80/20) using `train_test_split` from scikit-learn.
- **Saving Processed Data:**  
  The processed texts, labels, and label encoder are saved as `.pkl` files for efficient loading during training.  
  See [`training/preprocess.py`](training/preprocess.py).

### 3. Model Training

- **Model Choice:**  
  A RoBERTa transformer model (from HuggingFace Transformers) is used for text classification.
- **Tokenization:**  
  The text data is tokenized using the RoBERTa tokenizer.
- **Dataset & DataLoader:**  
  Custom PyTorch `Dataset` and `DataLoader` classes are used to efficiently batch and feed data to the model.
- **Fine-tuning:**  
  The RoBERTa model is fine-tuned on the training data using the AdamW optimizer, with optional mixed-precision (AMP) for speed.
- **Evaluation:**  
  After each epoch, the model is evaluated on the test set, and metrics like accuracy and a classification report are printed.
- **Saving the Model:**  
  The trained model and tokenizer are saved for later inference.  
  See [`training/train_roberta.py`](training/train_roberta.py).

### 4. Inference & Serving

- **Backend (FastAPI):**  
  The backend loads the trained model and exposes `/predict` and `/predict_batch` endpoints for document classification.
- **OCR & Prediction:**  
  Uploaded files are processed with OCR, then classified using the trained model.
- **Frontend (React):**  
  Users upload files via a web interface. Results (predicted label, confidence, etc.) are displayed in real time.

---

## 📦 Setup

**STEP 0 - CRUCIAL:**
- After you cloned the repo locally, **create a venv** in the root folder!

*If you want to use the pre-existing trained model* (NO NEED FOR NOW):
1. Download the `models/` folder and `data/` folder from [here](https://endava-my.sharepoint.com/:f:/r/personal/stefan_liute_endava_com/Documents/doc_classifier_extra?csf=1&web=1&e=qaiTWd)
2. Place them in the **root directory** of the project
3. If you stored them in the root_directory, make sure they are ignored by git (.gitignore file)

---

## Download Tesseract Windows [HERE](https://github.com/tesseract-ocr/tesseract/releases/download/5.5.0/tesseract-ocr-w64-setup-5.5.0.20241111.exe)
- install it in C:/Endava/EndevLocal
- edit environment variables (path)
- ![image](https://github.com/user-attachments/assets/cd55f593-3c1b-4b43-a1f1-7a8642f4a9a7)

---

## 🔧 Running the App Locally

### Backend (FastAPI)

```bash
pip install -r requirements.txt
uvicorn api.app:app --reload
```

### Frontend (React + Vite)

```bash
cd frontend
npm install
npm run dev
```
## 🛠️ Running with Docker

### 1. 📦 Prerequisites

Docker or Rancher Desktop with Docker CLI enabled

Clone this repo:

git clone https://github.com/<your-username>/DOC_CLASSIFIER.git
cd DOC_CLASSIFIER

### 2. 🐳 Build and Start Containers

docker compose up --build

This will:

- Build the FastAPI backend container

- Build the React + Vite frontend, served via NGINX

- Mount the models/ directory so the model and encoder are accessible

- Start both services in a shared Docker network

### 3. 🔗 Access the App

  🌐 Frontend: http://localhost:3000

  🧪 API Docs: http://localhost:8000/docs

### 4. 🛠 Common Docker Commands

#### Start containers
docker compose up --build

#### Stop containers
docker compose down

#### View container logs
docker compose logs -f backend

#### Access a container shell
docker exec -it doc_classifier-backend-1 bash

Once up, you can test API endpoints from Swagger UI or via frontend file upload
---

## 🧑‍💻 Contributing

This project is built by a 5-person team.  
See [CONTRIBUTE.md](./CONTRIBUTE.md) for role breakdowns, task assignments, and issue tracking guidelines.

---

## 🧪 Example Flow

1. Upload a `.pdf` or `.jpg`
2. Extract OCR text from the file
3. Classify the document type
4. View results in the UI

---

## 🧠 Tech Stack

- **Frontend:** React, Tailwind CSS, Axios
- **Backend:** FastAPI, Uvicorn
- **ML Model:** RoBERTa + OCR preprocessing (PyTorch, HuggingFace Transformers)
- **Deployment:** Local (no Docker)

---

## 📊 Visualization

- Use scripts in [`visualization/`](visualization/) (e.g., [`plot_label_distribution.py`](visualization/plot_label_distribution.py)) to analyze data and model performance.

---

## 📄 License

This project is for educational and research purposes.
