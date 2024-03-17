import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_homepage_response(client):
    """Test that the homepage responds with a 200 status code."""
    response = client.get('/')
    assert response.status_code == 200

def test_homepage_content(client):
    """Test that the homepage loads correctly and contains expected content."""
    response = client.get('/')
    assert "Choose your kind of Joke with the criterias" in response.data.decode()
    assert "<form" in response.data.decode()
    assert "name=\"category\"" in response.data.decode()
    assert "name=\"lang\"" in response.data.decode()
    assert "name=\"type\"" in response.data.decode()
    assert "name=\"blacklistFlags\"" in response.data.decode()
