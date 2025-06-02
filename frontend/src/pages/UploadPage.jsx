import Header from "../components/Header";
import Footer from "../components/Footer";
import { useState, useRef } from "react";
import { uploadAuto } from "../services/api";

function UploadPage() {
  const [selectedFiles, setSelectedFiles] = useState([]);
  const [isDragging, setIsDragging] = useState(false);
  const fileInputRef = useRef(null);
  const [results, setResults] = useState([]);

  const resetUpload = () => {
    setSelectedFiles([]);
    setResults([]);
  };

  const handleSubmit = async () => {
    if (selectedFiles.length === 0) return;

    try {
      const predictions = await uploadAuto(selectedFiles);
      console.log("API Response:", predictions);
      setResults(predictions);
    } catch (err) {
      console.error("Upload failed:", err);
      setResults([{ error: "Upload failed." }]);
    }
  };

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
    setResults([]);
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
    setResults([]);
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

          {/* Prediction Results */}
          {results.length > 0 && (
            <div className="mt-6 p-4 border border-fuchsia-600 rounded bg-gray-800 text-fuchsia-300 shadow-inner space-y-4">
              <h3 className="text-lg font-bold text-fuchsia-400 uppercase text-center">Prediction Results</h3>
              {results.map((res, idx) => (
                <div key={idx} className="p-3 border border-fuchsia-700 rounded text-sm bg-gray-900">
                  {res.error ? (
                    <p className="text-red-400">Error for {res.filename || `file ${idx + 1}`}: {res.error}</p>
                  ) : (
                    <>
                      <p><strong>Filename:</strong> {res.filename}</p>
                      <p><strong>Label:</strong> {res.label}</p>
                      <p><strong>Confidence:</strong> {res.confidence}</p>
                    </>
                  )}
                </div>
              ))}

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

          {/* Submit + Reset Buttons */}
          {selectedFiles.length > 0 && results.length === 0 && (
            <div className="text-center space-y-2">
              <button
                onClick={handleSubmit}
                className="px-4 py-2 bg-cyan-600 hover:bg-cyan-500 text-white font-semibold rounded transition duration-200"
              >
                Submit File{selectedFiles.length > 1 ? "s" : ""}
              </button>
              <button
                onClick={resetUpload}
                className="ml-4 px-4 py-2 bg-fuchsia-700 hover:bg-fuchsia-600 text-white font-semibold rounded transition duration-200"
              >
                Try Another File
              </button>
            </div>
          )}

        </div>
      </main>

      <Footer />
    </div>
  );
}

export default UploadPage;
