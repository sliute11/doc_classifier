import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000', // Adjust if your FastAPI runs on a different port
  headers: {
    'Content-Type': 'multipart/form-data'
  }
});

export const uploadDocument = async (file) => {
  const formData = new FormData();
  formData.append("file", file);

  const response = await api.post("/predict", formData);
  return response.data;
};
