from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import sqlite3

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE = "movie_game.db"

class MovieCreate(BaseModel):
    title: str
    genre: str
    script_id: int
    producer_id: int
    actor_ids: List[int]
    effect_ids: List[int]
    scandal_ids: List[int]

def query_db(query, args=(), one=False):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(query, args)
    result = cursor.fetchall()
    conn.commit()
    conn.close()
    return (result[0] if result else None) if one else result

@app.get("/scripts")
def get_scripts():
    rows = query_db("SELECT script_id, title FROM scripts")
    return [{"script_id": r[0], "title": r[1]} for r in rows]

@app.get("/producers")
def get_producers():
    rows = query_db("SELECT producer_id, name FROM producers")
    return [{"producer_id": r[0], "name": r[1]} for r in rows]

@app.get("/actors")
def get_actors():
    rows = query_db("SELECT actor_id, name FROM actors")
    return [{"actor_id": r[0], "name": r[1]} for r in rows]

@app.get("/effects")
def get_effects():
    rows = query_db("SELECT effect_id, type FROM effects")
    return [{"effect_id": r[0], "type": r[1]} for r in rows]

@app.get("/scandals")
def get_scandals():
    rows = query_db("SELECT scandal_id, description FROM scandals")
    return [{"scandal_id": r[0], "description": r[1]} for r in rows]

@app.post("/movies/create/")
def create_movie(movie: MovieCreate):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO movies (title, genre, script_id, producer_id) VALUES (?, ?, ?, ?)",
            (movie.title, movie.genre, movie.script_id, movie.producer_id)
        )
        movie_id = cursor.lastrowid

        for aid in movie.actor_ids:
            cursor.execute("INSERT INTO movie_actors (movie_id, actor_id) VALUES (?, ?)", (movie_id, aid))
        for eid in movie.effect_ids:
            cursor.execute("INSERT INTO movie_effects (movie_id, effect_id) VALUES (?, ?)", (movie_id, eid))
        for sid in movie.scandal_ids:
            cursor.execute("INSERT INTO movie_scandals (movie_id, scandal_id) VALUES (?, ?)", (movie_id, sid))

        conn.commit()
        return {"message": "Movie created", "movie_id": movie_id}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()