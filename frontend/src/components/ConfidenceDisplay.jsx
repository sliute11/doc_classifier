function ConfidenceDisplay({ confidence }) {
  return (
    <p className="text-sm text-fuchsia-200">
      <strong>Confidence:</strong> {confidence !== null ? confidence : "N/A"}
    </p>
  );
}

export default ConfidenceDisplay;
