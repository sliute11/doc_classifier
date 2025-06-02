import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000', // Adjust if your FastAPI runs on a different port
  headers: {
    'Content-Type': 'multipart/form-data'
  }
});

export const uploadAuto = async (files) => {
  const formData = new FormData();

  if (files.length === 1) {
    formData.append("file", files[0]);
    const response = await api.post("/predict", formData);
    return [response.data];  // Wrap in array for consistency
  } else {
    files.forEach(file => formData.append("files", file));
    const response = await api.post("/predict_batch", formData);
    return response.data.predictions;
  }
};
