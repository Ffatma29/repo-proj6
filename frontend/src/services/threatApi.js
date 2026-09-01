import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export const detectThreat = async (log) => {
  const response = await axios.post(`${API_URL}/api/detect`, log);
  return response.data;
};

export const getThreats = async () => {
  const response = await axios.get(`${API_URL}/api/threats`);
  return response.data;
};

export const getThreatStats = async () => {
  const response = await axios.get(`${API_URL}/api/threats/stats`);
  return response.data;
};

export const connectThreatWebSocket = (onMessage) => {
  const socket = new WebSocket("ws://127.0.0.1:8000/ws/threats");

  socket.onmessage = (event) => {
    const data = JSON.parse(event.data);
    onMessage(data);
  };

  socket.onerror = (error) => {
    console.error("WebSocket error:", error);
  };

  return socket;
};
