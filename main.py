from fastapi import FastAPI
from utils import get_affirmations


app = FastAPI()

@app.get("/affimations/{mood}")
async def fetch_affirmation(mood: str):
    return get_affirmations(mood)