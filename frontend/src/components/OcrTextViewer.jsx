function OcrTextViewer({ text }) {
  return (
    <div className="w-full max-h-60 overflow-y-auto p-3 bg-gray-900 rounded text-sm border border-fuchsia-800 whitespace-pre-line">
      {text || "[OCR text will appear here]"}
    </div>
  );
}

export default OcrTextViewer;
