from datetime import datetime
from uuid import uuid4

from app.db.schema import Challenge, Leaderboard


def test_challenge():
    challenge = Challenge(
        uuid=uuid4(),
        day_id=1,
        title="Test Challenge",
        tags=["test", "challenge"],
        open_at=datetime.now(),
        created_by="test",
        content="<h1>Test Challenge</h1>",
    )
    assert challenge.uuid
    assert challenge.day_id == 1
    assert challenge.title == "Test Challenge"
    assert challenge.tags == ["test", "challenge"]
    assert challenge.open_at
    assert challenge.created_by == "test"
    assert challenge.content == "<h1>Test Challenge</h1>"
    assert challenge.ConfigDict.from_attributes


def test_leaderboard():
    leaderboard = Leaderboard(
        user_uuid=uuid4(),
        username="test",
        profile_url="https://example.com",
        score=1,
        mate=1,
        total=2,
    )
    assert leaderboard.user_uuid
    assert leaderboard.username == "test"
    assert leaderboard.profile_url == "https://example.com"
    assert leaderboard.score == 1
    assert leaderboard.mate == 1
    assert leaderboard.total == 2
    assert leaderboard.ConfigDict.from_attributes
