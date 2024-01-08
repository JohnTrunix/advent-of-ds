from datetime import datetime
from uuid import uuid4

from app.db.schema import Challenge, Leaderboard, User, UserCreate, UserRead


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
        avatar_url="https://example.com",
        score=1,
        mate=1,
        total=2,
    )
    assert leaderboard.user_uuid
    assert leaderboard.username == "test"
    assert leaderboard.profile_url == "https://example.com"
    assert leaderboard.avatar_url == "https://example.com"
    assert leaderboard.score == 1
    assert leaderboard.mate == 1
    assert leaderboard.total == 2
    assert leaderboard.ConfigDict.from_attributes


def test_user():
    user = User(
        username="test",
        email="test@email.com",
        avatar_url="https://example.com",
        profile_url="https://example.com",
        oauth_token="test",
    )
    assert user.username == "test"
    assert user.email == "test@email.com"
    assert user.avatar_url == "https://example.com"
    assert user.profile_url == "https://example.com"
    assert user.oauth_token == "test"
    assert user.ConfigDict.from_attributes


def test_user_create():
    user_create = UserCreate(
        github_id="test",
        username="test",
        email="test@email.com",
        avatar_url="https://example.com",
        profile_url="https://example.com",
        oauth_token="test",
    )
    assert user_create.github_id == "test"
    assert user_create.username == "test"
    assert user_create.email == "test@email.com"
    assert user_create.avatar_url == "https://example.com"
    assert user_create.profile_url == "https://example.com"
    assert user_create.oauth_token == "test"
    assert user_create.ConfigDict.from_attributes


def test_user_read():
    user_read = UserRead(
        uuid=uuid4(),
        github_id="test",
        username="test",
        email="test@email.com",
        avatar_url="https://example.com",
        profile_url="https://example.com",
        oauth_token="test",
    )
    assert user_read.uuid
    assert user_read.github_id == "test"
    assert user_read.username == "test"
    assert user_read.email == "test@email.com"
    assert user_read.profile_url == "https://example.com"
    assert user_read.oauth_token == "test"
    assert user_read.ConfigDict.from_attributes
