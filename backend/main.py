from fastapi import FastAPI
from pydantic import BaseModel
from analysis import analyze_game

app = FastAPI()
class GameRequest(BaseModel):
    pgn: str

@app.get("/")
def read_root():
    return {"message": "Chess Analyzer API is running"}

@app.post("/analyze")
def analyze(request: GameRequest):
    results = analyze_game(request.pgn)
    if results is None:
        return {"error": "Invalid PGN"}
    return {"analysis": results}
    