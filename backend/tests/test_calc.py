from app.calc import add


def test_add():
    result = add(1, 2)
    assert result == 3
