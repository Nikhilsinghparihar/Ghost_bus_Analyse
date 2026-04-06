import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'
// import TrackingMap from './blank.jsx'
import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:5000/"
});

export default API;

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
    {/* <TrackingMap /> */}
  </StrictMode>,
)