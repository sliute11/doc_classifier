function PredictionLabel({ label }) {
  return (
    <div className="text-center">
      <h3 className="text-lg font-bold text-fuchsia-400 uppercase mb-1">
        Predicted Document Type
      </h3>
      <p className="text-base">{label || "[Waiting for prediction]"}</p>
    </div>
  );
}

export default PredictionLabel;
