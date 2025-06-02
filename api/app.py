from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import os
from tempfile import NamedTemporaryFile
from predictors.predict_document_type import predict_document_type  # import your logic

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # my Vite frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Welcome to the document classifier! Use /predict for one file or /predict_batch for multiple files."}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    suffix = os.path.splitext(file.filename)[1]
    with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    try:
        label, confidence = predict_document_type(tmp_path)
    except Exception as e:
        os.remove(tmp_path)
        return {"error": str(e)}

    os.remove(tmp_path)

    return {
        "filename": file.filename,
        "label": label,
        "confidence": round(confidence, 4)
    }

@app.post("/predict_batch")
async def predict_batch(files: list[UploadFile] = File(...)):
    results = []

    for file in files:
        suffix = os.path.splitext(file.filename)[1]
        with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(await file.read())
            tmp_path = tmp.name

        try:
            label, confidence = predict_document_type(tmp_path)
            results.append({
                "filename": file.filename,
                "label": label,
                "confidence": round(confidence, 4)
            })
        except Exception as e:
            results.append({
                "filename": file.filename,
                "error": str(e)
            })
        finally:
            os.remove(tmp_path)

    return {"predictions": results}
