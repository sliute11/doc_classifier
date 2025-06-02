
# 🧩 Contribution Guide – Document Classifier Frontend

Welcome to the team! This guide outlines how to contribute to the frontend for our FastAPI-based document classifier. It includes task assignments, issue descriptions, and workflow details.

---

## 🧑‍🤝‍🧑 Team Roles & Responsibilities

| Member | Role | Key Responsibilities |
|--------|------|----------------------|
| A | Frontend UI | Build React + Tailwind components |
| B | API Integration | Connect React frontend to FastAPI backend |
| C | FastAPI Backend | Serve predictions + OCR with FastAPI |
| D | Local Dev & Docs | Setup instructions & cross-platform testing |
| E | QA & Docs | Testing + maintaining README |
| X | 'Project Manager' | GitHub board, PR reviews, coordination |

---

## 🔁 GitHub Workflow

- **Branches**: First create the branch `<name_of_your_assigned_issue>` ==> switch on the created branch ==> work on the created branch (IMPORTANT!)
- **Pull Requests**: Always open PRs against `main` with 1 reviewer minimum
- **Labels**: `frontend`, `backend`, `docs`, `qa`, `api`, `bug`, `enhancement`
- **Project Board**: Use `To Do`, `In Progress`, `Review`, `Done`

---

## 📝 Issue Assignments

### 👤 Member A – Frontend UI

**Issue 1: Scaffold React Project Structure**
- Create base React project (Vite or CRA)
- Tailwind CSS config
- Folder setup (`components`, `pages`)

**Issue 2: Implement Document Upload UI**
- File picker + drag-and-drop
- File name display
- Accept .pdf, .jpg, .png

**Issue 3: Add Layout and Tailwind Styling**
- Header, footer, responsive layout

**Issue 4: Build Results Display Components**
- OCR viewer + prediction label display

---

### 👤 Member B – API Integration

**Issue 1: Create Axios Service**
- Base URL config
- POST to `/predict`

**Issue 2: Implement File Upload Logic**
- Capture FormData
- Handle response JSON

**Issue 3: Handle States**
- Show loading, errors, and results

**Issue 4: File Validation**
- Restrict file size/type on client

---

### 👤 Member C – FastAPI Backend

**Issue 1: Review and Clean `/predict`**
- Accept file
- Return OCR + label in JSON

**Issue 2: Refactor Logic**
- Modularize OCR + prediction

**Issue 3: Add CORS Middleware**
- Allow `localhost:3000` requests

**Issue 4: Error Handling**
- Return structured 422/500 responses

---

### 👤 Member D – Local Dev Environment

**Issue 1: Document Backend Setup**
- Python version, dependencies, run command

**Issue 2: Document Frontend Setup**
- Node/npm, run command, URLs

**Issue 3: Cross-Platform Test**
- Try on Windows + Mac/Linux

**Issue 4: Add .env.example + Notes**
- Include VITE_API_BASE_URL, etc.

---

### 👤 Member E – QA & Docs

**Issue 1: Write Main README**
- Overview, usage, setup, contribution

**Issue 2: Functional QA**
- Upload tests, edge cases, report issues

**Issue 3: Final Sprint Validation**
- Checklist for demo/handoff

---

## ✅ Final Checklist for Handoff

- [x] Frontend connects to FastAPI successfully
- [x] Upload, OCR, and prediction flow complete
- [ ] Docs are updated and clear
- [ ] All project board cards moved to `Done`
