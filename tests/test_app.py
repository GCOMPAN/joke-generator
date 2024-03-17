import pytest
from app import app, get_categories


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index(client):
    """Ensure the index page loads correctly."""
    response = client.get('/')
    assert response.status_code == 200


def test_get_categories():
    """Ensure that categories are fetched correctly."""
    categories = get_categories()
    assert 'Any' in categories  # Assuming 'Any' is always a valid category


def test_joke_post(client):
    """Ensure posting data to the form returns a joke."""
    response = client.post('/', data=dict(category='Any', lang='en', type='any'))
    assert "Click the button to get a joke.." not in response.data.decode()
