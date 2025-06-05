import React from "react";

function PredictionAccuracy({ results }) {
  // Only count if both predicted and actual label are present
  const matched = results.filter(
    (res) => res.label && res.actual_label && res.label === res.actual_label
  ).length;
  const total = results.filter(
    (res) => res.label && res.actual_label
  ).length;

  if (total === 0) return null;

  const accuracy = ((matched / total) * 100).toFixed(2);

  return (
    <div className="text-center my-4">
      <p className="text-lime-300 font-semibold">
        Matched: {matched} / {total} ({accuracy}% accuracy)
      </p>
    </div>
  );
}

export default PredictionAccuracy;