from fastapi import FastAPI
from utils import get_affirmations


app = FastAPI()

@app.get("/affimations/{mood}")
async def fetch_affirmation(mood: str):

    return get_affirmations(mood)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
