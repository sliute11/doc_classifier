
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
├── api/                    # FastAPI backend
├── predictors/             # Model prediction logic
├── processing/             # OCR and data extraction
├── training/               # Preprocessing and model training
├── requirements.txt        # Python dependencies
├── frontend/               # React app (if scaffolded)
├── docs/                   # Dev setup instructions
├── CONTRIBUTE.md           # Team roles and issue assignments
└── README.md               # This file
```

---

## 📦 Setup

**STEP 0 - CRUCIAL:**
- After you cloned the repo locally, **create a venv** in the root folder!

*If you want to use the pre-existing trained model* (NO NEED FOR NOW):
*1. Download the `models/` folder and `data/` folder from [here](https://endava-my.sharepoint.com/:f:/r/personal/stefan_liute_endava_com/Documents/doc_classifier_extra?csf=1&web=1&e=qaiTWd)*
*2. Place them in the **root directory** of the project*
*3. If you stored them in the root_directory, make sure they are ignored by git (.gitignore file)*

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
- **ML Model:** RoBERTa + OCR preprocessing
- **Deployment:** Local (no Docker)

---

## 📄 License

This project is for educational and research purposes.
