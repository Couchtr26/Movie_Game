# 🎬 Movie Game Backend (FastAPI + SQLite)

This project is a simulation engine and backend API for managing a fictional movie production game. It is built using **FastAPI** and **SQLite**, demonstrating database relationships, random data generation, and RESTful interaction.

---

## 📽️ Demo Video
https://youtu.be/nf5_B6xl-Bc 
This video demonstrates core functionality including:
- Random movie generation
- Actor and producer queries
- ![Producer Query](./Screenshot_2025-07-03_180650.png)
- Live database interaction via FastAPI

---

## 💾 Features

- **SQLite database** with multiple related tables (`Movies`, `Actors`, `Producers`, `Scandals`, etc.)
- ![Movie Query](./Screenshot_2025-07-03_180629.png)
- **Random movie generator** that creates and populates full records
- ![Creating a random movie via API](./Screenshot_2025-07-03_180607.png)
- **Scandals and casting** assigned to movies randomly
- **FastAPI** endpoints for:
  - Creating a new random movie
  - Viewing movie details
  - Searching actors, producers, and movies
- Full error handling for missing data or database issues

---

## 🧱 Database Schema Overview

- `Movies`  
- `Actors`  
- `Producers`  
- `Genres`  
- `Scandals`  
- `Movie_Cast` (many-to-many relationship)  
- `Movie_Scandal` (many-to-many relationship)

---

## 🚀 Run the Server

1. Install dependencies:
    ```bash
    pip install fastapi uvicorn
    ```

2. Start the server:
    ```bash
    uvicorn main:app --reload
    ```

3. Access the documentation at:
    ```
    http://127.0.0.1:8000/docs
    ```

---

## 🔧 Still in Progress

- `/movies/{id}/full` endpoint is under repair
- More genre and budget logic to be added
- UI integration coming soon

---

## 🙋 About

This project was built solo as part of a backend showcase. It demonstrates hands-on experience with API development, relational data modeling, and procedural content generation.

## 🖥️ Server Running Example

Below is a snapshot of the FastAPI server running successfully, handling real HTTP requests:

![API running](./Screenshot_2025-07-03_180734.png)

This confirms that the API was operational, connected to the SQLite database, and handled multiple endpoints during live testing.

📄 License
MIT License — free to use, modify, and distribute.

© 2025 Thomas Couch — Grey Knight Software
