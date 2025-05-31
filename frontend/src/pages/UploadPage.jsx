import { useState, useRef } from "react";

function UploadPage() {
  const [selectedFiles, setSelectedFiles] = useState([]);
  const [isDragging, setIsDragging] = useState(false);
  const fileInputRef = useRef(null);

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
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100 p-6">
      <h1 className="text-3xl font-bold text-gray-800 mb-6">Upload a Document</h1>

      {/* Dropzone */}
      <div
        onClick={() => fileInputRef.current.click()}
        onDragOver={(e) => {
          e.preventDefault();
          setIsDragging(true);
        }}
        onDragLeave={() => setIsDragging(false)}
        onDrop={handleDrop}
        className={`w-full max-w-md h-40 border-2 rounded-lg flex items-center justify-center text-center cursor-pointer transition-colors
          ${isDragging ? "border-blue-500 bg-blue-100" : "border-dashed border-gray-400 bg-white"}`}
      >
        <p className="text-gray-600">
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
        <ul className="mt-4 text-sm text-gray-800 space-y-1 text-center">
          {selectedFiles.map((file, idx) => (
            <li key={idx}>
              {idx + 1}. <strong>{file.name}</strong>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default UploadPage;
