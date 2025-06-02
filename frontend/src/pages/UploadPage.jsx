import Header from "../components/Header";
import Footer from "../components/Footer";
// import OcrTextViewer from "../components/OcrTextViewer";
import FilenameDisplay from "../components/FilenameDisplay";
import ConfidenceDisplay from "../components/ConfidenceDisplay";
import PredictionLabel from "../components/PredictionLabel";
import { uploadDocument } from "../services/api";
import { useState, useRef } from "react";

function UploadPage() {
  const [selectedFiles, setSelectedFiles] = useState([]);
  const [isDragging, setIsDragging] = useState(false);
  const fileInputRef = useRef(null);
  const [filename, setFilename] = useState("");
  const [confidence, setConfidence] = useState(null);

  
  const resetUpload = () => {
  setSelectedFiles([]);
  setPredictedType("Invoice"); // Or "" if you'd prefer blank
  // setOcrResult("");
  };

  // adding handler sumbit
  const handleSubmit = async () => {
    if (selectedFiles.length === 0) return;

    try {
      const response = await uploadDocument(selectedFiles[0]);
      console.log("API Response:", response);

      setPredictedType(response.predicted_type || response.label || "Unknown");
      // setOcrResult(response.ocr_text || "No OCR text found.");
      setFilename(response.filename || "");
      setConfidence(response.confidence || null);
    } catch (err) {
      console.error("Upload failed:", err);
      setPredictedType("Error");
      setOcrResult("An error occurred while processing the document.");
      setFilename("");
      setConfidence(null);
    }
  };


  const [predictedType, setPredictedType] = useState("Invoice");
  // const [ocrResult, setOcrResult] = useState(`This is a simulated OCR output.
  //   It will eventually be replaced by real extracted text from the document you upload.
  //   zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
  //   zzzzzzzzzzzzzzzzzzzzzzzzzzzThis is a simulated OCR output.
  //   It will eventually be replaced by real extracted text from the document you upload.
  //   zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
  //   zzzzzzzzzzzzzzzzzzzzzzzzzzzThis is a simulated OCR output.
  //   It will eventually be replaced by real extracted text from the document you upload.
  //   zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
  //   zzzzzzzzzzzzzzzzzzzzzzzzzzzThis is a simulated OCR output.
  //   It will eventually be replaced by real extracted text from the document you upload.
  //   zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
  //   zzzzzzzzzzzzzzzzzzzzzzzzzzzThis is a simulated OCR output.
  //   It will eventually be replaced by real extracted text from the document you upload.
  //   zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
  //   zzzzzzzzzzzzzzzzzzzzzzzzzzzThis is a simulated OCR output.
  //   It will eventually be replaced by real extracted text from the document you upload.
  //   zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
  //   zzzzzzzzzzzzzzzzzzzzzzzzzzzThis is a simulated OCR output.
  //   It will eventually be replaced by real extracted text from the document you upload.
  //   zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
  //   zzzzzzzzzzzzzzzzzzzzzzzzzzzThis is a simulated OCR output.
  //   It will eventually be replaced by real extracted text from the document you upload.
  //   zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
  //   zzzzzzzzzzzzzzzzzzzzzzzzzzz`);


  const handleFileChange = (e) => {
    const files = Array.from(e.target.files);
    const validExtensions = [".pdf", ".jpg", ".jpeg", ".png", ".tif"];

    const validFiles = files.filter(file => {
      const ext = file.name.toLowerCase().slice(file.name.lastIndexOf("."));
      return validExtensions.includes(ext);
    });

    if (validFiles.length === 0) {
      alert("Only PDF, JPG, JPEG, PNG, and TIF files are allowed.");
      return;
    }

    setSelectedFiles(validFiles);
  };

  const handleDrop = (e) => {
    e.preventDefault();
    setIsDragging(false);

    const files = Array.from(e.dataTransfer.files);
    const validExtensions = [".pdf", ".jpg", ".jpeg", ".png", ".tif"];

    const validFiles = files.filter(file => {
      const ext = file.name.toLowerCase().slice(file.name.lastIndexOf("."));
      return validExtensions.includes(ext);
    });

    if (validFiles.length === 0) {
      alert("Only PDF, JPG, JPEG, PNG, and TIF files are allowed.");
      return;
    }

    setSelectedFiles(validFiles);
    e.dataTransfer.clearData();
  };

  return (
    <div className="min-h-screen flex flex-col bg-gray-950 text-gray-100 font-mono">
      <Header />

      <main className="flex flex-col items-center justify-center flex-grow px-4 py-8">
        <div className="w-full max-w-4xl bg-gray-900 border border-cyan-700 shadow-lg p-6 rounded-lg space-y-6">

          <h2 className="text-2xl font-bold text-cyan-400 tracking-widest text-center uppercase">
            Upload Documents
          </h2>

          {/* Dropzone */}
          <div
            onClick={() => fileInputRef.current.click()}
            onDragOver={(e) => {
              e.preventDefault();
              setIsDragging(true);
            }}
            onDragLeave={() => setIsDragging(false)}
            onDrop={handleDrop}
            className={`w-full h-40 border-2 rounded-lg flex items-center justify-center text-center cursor-pointer transition-all duration-300
              ${isDragging ? "border-cyan-400 bg-cyan-950/40 shadow-cyan-500/30" : "border-cyan-700 border-dashed bg-gray-800 hover:shadow-cyan-500/20"}`}
          >
            <p className="text-cyan-200">
              Drag & drop PDF or image files here,<br />or click to browse.
            </p>
          </div>

          {/* Hidden File Input */}
          <input
            type="file"
            multiple
            ref={fileInputRef}
            onChange={handleFileChange}
            accept=".pdf,.jpg,.jpeg,.png,.tif"
            className="hidden"
          />

          {/* File List */}
          {selectedFiles.length > 0 && (
            <ul className="list-decimal list-inside text-sm text-lime-400 space-y-1 text-center">
              {selectedFiles.map((file, idx) => (
                <li key={idx}>
                  {file.name}
                </li>
              ))}
            </ul>
          )}

        {/* Placeholder Result Block */}

        {selectedFiles.length > 0 && (
        <div className="mt-6 p-4 border border-fuchsia-600 rounded bg-gray-800 text-fuchsia-300 shadow-inner space-y-6">
            <PredictionLabel label={predictedType} />

            <div className="text-center space-y-1">
              <FilenameDisplay filename={filename} />
              <ConfidenceDisplay confidence={confidence} />
            </div>


            {/* EXTRACTED OCR TEXT (TO BE ADDED LATER IF WE WANT IT) - OR maybe we could add an option to save it locally. */}
            {/* <div className="w-full">
            <h3 className="text-lg font-bold text-fuchsia-400 uppercase mb-2">Extracted OCR Text</h3>
            <OcrTextViewer text={ocrResult} />
            </div> */}

        {/* Submit button placeholder */}
        {selectedFiles.length > 0 && (
          <div className="text-center">
            <button
              onClick={handleSubmit}
              className="mt-4 px-4 py-2 bg-cyan-600 hover:bg-cyan-500 text-white font-semibold rounded transition duration-200"
            >
              Submit File
            </button>
          </div>
        )}


            {/* ✅ Try Another File Button */}
            <div className="text-center">
            <button
                onClick={resetUpload}
                className="mt-4 px-4 py-2 bg-fuchsia-700 hover:bg-fuchsia-600 text-white font-semibold rounded transition duration-200"
            >
                Try Another File
            </button>
            </div>
        </div>
        )}

        </div>
      </main>

      <Footer />
    </div>
  );
}

export default UploadPage;
