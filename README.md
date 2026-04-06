# 🗳️ Online Voting System (React + Flask + SQLite)

A modern **full-stack online voting system** built using **React (Frontend)** and **Flask (Backend)** with **SQLite database**.
This project simulates a real-world election system with secure voting, live updates, and an interactive admin dashboard.

---

## 🚀 Features

### 👤 User Module

* User registration with Aadhaar, mobile number, and personal details
* OTP-based login system (simulated)
* Secure one-time voting (prevents duplicate votes)
* State & city selection for voting

### 🗳️ Voting System

* Vote for political parties based on selected state
* Real-time vote submission using API
* Duplicate vote prevention using Aadhaar

### 📊 Admin Dashboard

* Live vote count updates
* 🏆 Winning party display
* 📈 Party-wise vote percentage
* 🏙️ City-wise and state-wise analytics
* 📊 Pie and Bar charts (Chart.js)
* 🔍 Aadhaar-based voter search

### 🧠 Advanced Features

* Multi-state comparison (Bar Chart)
* Dynamic chart colors
* Export voting data (CSV)
* Clean and modern UI design

---

## 🛠️ Tech Stack

### Frontend

* React.js
* Chart.js (react-chartjs-2)
* Axios
* Socket.IO Client

### Backend

* Flask (Python)
* Flask-CORS
* Flask-SocketIO

### Database

* SQLite (lightweight, no installation required)

---

## 🗄️ Database Structure

### Users Table

* id
* name
* mobile
* aadhaar (unique)
* city
* state

### Votes Table

* id
* aadhaar
* party

---

## 🔌 API Endpoints

| Method | Endpoint         | Description          |
| ------ | ---------------- | -------------------- |
| POST   | /register        | Register new user    |
| POST   | /vote            | Submit vote          |
| GET    | /results         | Get vote counts      |
| GET    | /search/:aadhaar | Search voter details |

---

## ▶️ How to Run

### 🔹 Backend (Flask)

```bash
python app.py
```

### 🔹 Frontend (React)

```bash
npm install
npm start
```

---

## 🔐 Security Features

* Aadhaar-based unique voting
* Duplicate vote prevention
* Backend validation for all operations
* Safe SQL queries using parameterized inputs

---

## 📌 Future Enhancements

* 🔐 Firebase OTP (real SMS verification)
* 🌐 Deployment (Vercel + Render)
* 🗺️ Map-based vote visualization
* 🧠 AI-based election prediction
* 🪪 Aadhaar verification API integration
* 🔗 Blockchain-based voting system

---

## 📸 Screenshots

* Home Page
* Voting Page
* Admin Dashboard
* Charts & Analytics

---

## 👨‍💻 Author

**NIKHIL SINGH PARIHAR**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to contribute!
