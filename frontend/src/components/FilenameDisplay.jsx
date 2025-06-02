function FilenameDisplay({ filename }) {
  return (
    <p className="text-sm text-fuchsia-200">
      <strong>Filename:</strong> {filename || "N/A"}
    </p>
  );
}

export default FilenameDisplay;
