import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_homepage_response(client):
    response = client.get('/')
    assert response.status_code == 200