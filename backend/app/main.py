from enum import Enum

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import challenges, leaderboard, login


class Tags(Enum):
    root = "root"
    leaderboard = "leaderboard"
    challenges = "challenges"
    login = "login"


origins: list[str] = [
    # "http://localhost:4200",
    "*",
]

app: FastAPI = FastAPI(
    title="Advent of Data Science",
    description="Backend for the Advent of Data Science (AoDS) challenge.",
    version="0.1.0",
    openapi_tags=[
        {"name": Tags.root, "description": "Root endpoint"},
        {"name": Tags.challenges, "description": "Challenges endpoint"},
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
app.include_router(challenges.router, prefix="/v1", tags=[Tags.challenges])
app.include_router(login.router, prefix="/v1", tags=[Tags.login])


@app.get("/", tags=[Tags.root])
async def health() -> dict[str, bool]:
    return {"backend": True}
