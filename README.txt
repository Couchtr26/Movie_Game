# 🎬 Movie Game – Full Stack Demo App

Build and simulate custom movies from scripts, producers, actors, effects, and scandals.  
This app is designed to showcase full-stack capabilities using **React + FastAPI + SQLite**, fully containerized with Docker.

---

## ✨ Features

- 🎥 Create a movie from existing data
- 🧠 Combine creative inputs: producers, actors, effects, and scandals
- 📄 Backend powered by FastAPI (Python)
- 🌐 Frontend built in React + TailwindCSS
- 🗂 Connected to a real SQLite game database
- 🐳 Dockerized for quick deployment and demo access

---

## 🚀 Quick Start (with Docker)

### 🐋 Prerequisites:
- [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/install/)

### 🔧 Steps:
```bash
git clone https://github.com/Couchtr26/movie-builder.git
cd movie-builder
docker-compose up --build
Frontend UI: http://localhost:3000

Backend API: http://localhost:8000

🔍 Manual Setup (Local Dev)
Backend (FastAPI):
bash
Copy
Edit
cd backend
pip install fastapi uvicorn
uvicorn main:app --reload
Frontend (React):
bash
Copy
Edit
cd frontend
npm install
npm start