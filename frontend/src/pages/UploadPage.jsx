import { useState, useRef } from "react";

function UploadPage() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [isDragging, setIsDragging] = useState(false);
  const fileInputRef = useRef(null);

  const handleFile = (file) => {
    if (!file) return;

    const validExtensions = [".pdf", ".jpg", ".jpeg", ".png", ".tif"];
    const fileName = file.name.toLowerCase();
    const fileExtension = fileName.substring(fileName.lastIndexOf("."));

    if (!validExtensions.includes(fileExtension)) {
      alert("Only PDF, JPG, TIF, and PNG files are allowed.");
      return;
    }

    setSelectedFile(file);
  };


  const handleFileChange = (e) => {
    handleFile(e.target.files[0]);
  };

  const handleDrop = (e) => {
    e.preventDefault();
    setIsDragging(false);
    if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
      handleFile(e.dataTransfer.files[0]);
      e.dataTransfer.clearData();
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center justify-center p-4">
      <h1 className="text-3xl font-bold mb-6 text-gray-800">Upload a Document</h1>

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
          ${isDragging ? "border-blue-500 bg-blue-50" : "border-dashed border-gray-400 bg-white"}`}
      >
        <p className="text-gray-600">
          Drag & drop a PDF or image here,<br />or click to browse.
        </p>
      </div>

      {/* Hidden File Input */}
      <input
        type="file"
        ref={fileInputRef}
        onChange={handleFileChange}
        accept=".pdf,.jpg,.jpeg,.png, .tif"
        className="hidden"
      />

      {/* File Preview */}
      {selectedFile && (
        <p className="mt-4 text-sm text-gray-700">
          Selected: <strong>{selectedFile.name}</strong>
        </p>
      )}
    </div>
  );
}

export default UploadPage;
