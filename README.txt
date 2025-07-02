Movie Game – Full Stack Demo App Backend
Build and simulate custom movies combining producers, actors, special effects, and scandals. This backend API is built with FastAPI, SQLAlchemy, and SQLite, designed to serve a React frontend and showcase a full-stack architecture.

✨ Features
Create, retrieve, and manage movies with multiple actors and a producer

Store and relate producers, actors, effects, and scandals

SQLite database with SQLAlchemy ORM models

FastAPI REST endpoints with input validation via Pydantic schemas

CORS enabled for seamless frontend integration

Easily extensible to add more complex game logic

🚀 Getting Started
Prerequisites
Python 3.8+

pip

Installation & Running
Clone the repository:

bash
Copy
Edit
git clone https://github.com/Couchtr26/movie-builder.git
cd movie-builder/backend
Create and activate a virtual environment (recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the API server:

bash
Copy
Edit
uvicorn main:app --reload
Open your browser or API client and visit:

arduino
Copy
Edit
http://localhost:8000
Visit the interactive API docs at:

bash
Copy
Edit
http://localhost:8000/docs
🔧 Project Structure
main.py: FastAPI app entry point and route definitions

models.py: SQLAlchemy ORM models for movies, actors, producers

schemas.py: Pydantic models for request validation and response serialization

crud.py: Database access functions encapsulating create/read operations

database.py: Database connection and session setup

🛠 Technologies Used
FastAPI — High-performance Python web framework for APIs

SQLAlchemy — ORM for relational database mapping

SQLite — Lightweight, file-based database for development/demo

Pydantic — Data validation and parsing using Python type annotations

📈 Future Improvements
Add update and delete endpoints

Implement authentication/authorization

Expand game logic (e.g., scoring, player stats)

Connect to a React or other frontend client

Integrate Docker for easy deployment

🤝 Contributing
Contributions, suggestions, and bug reports are welcome! Feel free to fork the repo and open a pull request or issue.

📄 License
MIT License — free to use, modify, and distribute.

© 2025 Thomas Couch — Grey Knight Software