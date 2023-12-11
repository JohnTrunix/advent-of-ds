import json
from datetime import datetime

from litestar import Litestar, get
from litestar.config.cors import CORSConfig

from .models.leaderboard import Leaderboard


@get("/")
async def index() -> dict[str, str]:
    """
    Index route

    :return: health check
    """
    return {"status": "ok"}


@get("/leaderboard")
async def leaderboard() -> Leaderboard:
    """
    Returns the leaderboard sorted by score + coffees per user

    :return: sorted leaderboard
    """
    with open("app/mocking/leaderboard.json", "r") as file:
        board: Leaderboard = Leaderboard(
            entries=json.load(file), request_time=datetime.now()
        )

    # Sort by score + coffees
    board.entries.sort(
        key=lambda entry: entry.score + entry.coffees, reverse=True
    )
    return board


cors_config = CORSConfig(allow_origins=["http://localhost:4200/*"])
# Litestar App
app: Litestar = Litestar(
    route_handlers=[index, leaderboard], cors_config=cors_config, debug=True
)
