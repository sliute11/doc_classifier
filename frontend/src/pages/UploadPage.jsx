import { useState } from "react";

function UploadPage() {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (!file) return;
    if (![
      "application/pdf", 
      "image/jpeg", 
      "image/png", 
      "image/tif"
    ].includes(file.type)) {
      alert("Only PDF, JPG, TIF, and PNG files are allowed.");
      return;
    }
    setSelectedFile(file);
  };

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center justify-center p-4">
      <h1 className="text-3xl font-bold mb-6 text-gray-800">Upload a Document</h1>

      <input
        type="file"
        accept=
        ".pdf, .jpg, .jpeg, .png, .tif"
        onChange={handleFileChange}
        className="mb-4"
      />

      {selectedFile && (
        <p className="text-sm text-gray-600">
          Selected: <strong>{selectedFile.name}</strong>
        </p>
      )}
    </div>
  );
}

export default UploadPage;
