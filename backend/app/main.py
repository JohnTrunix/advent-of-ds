from enum import Enum

from fastapi import FastAPI

from app.routes import leaderboard


class Tags(Enum):
    root = "root"
    leaderboard = "leaderboard"


app: FastAPI = FastAPI(
    title="Advent of Data Science",
    description="Backend for the Advent of Data Science (AoDS) challenge.",
    version="0.1.0",
    openapi_tags=[
        {"name": Tags.root, "description": "Root endpoint"},
        {"name": Tags.leaderboard, "description": "Leaderboard endpoint"},
    ],
)

app.include_router(leaderboard.router, prefix="/v1", tags=[Tags.leaderboard])


@app.get("/", tags=[Tags.root])
async def health() -> dict[str, bool]:
    return {"backend": True}
