from enum import Enum

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import leaderboard


class Tags(Enum):
    root = "root"
    leaderboard = "leaderboard"


origins: list[str] = [
    "http://localhost:4200",
]

app: FastAPI = FastAPI(
    title="Advent of Data Science",
    description="Backend for the Advent of Data Science (AoDS) challenge.",
    version="0.1.0",
    openapi_tags=[
        {"name": Tags.root, "description": "Root endpoint"},
        {"name": Tags.leaderboard, "description": "Leaderboard endpoint"},
    ],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["GET"],
    allow_headers=["*"],
)

app.include_router(leaderboard.router, prefix="/v1", tags=[Tags.leaderboard])


@app.get("/", tags=[Tags.root])
async def health() -> dict[str, bool]:
    return {"backend": True}
