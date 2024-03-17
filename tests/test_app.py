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
    assert "Click the button to get a joke..." in response.data.decode()

def test_get_categories():
    """Ensure that categories are fetched correctly."""
    categories = get_categories()
    assert 'Any' in categories

@pytest.mark.parametrize("category, lang, joke_type", [
    ('Any', 'en', 'any'),
    ('Programming', 'fr', 'single'),
    ('Misc', 'de', 'twopart'),
])
def test_joke_post_different_options(client, category, lang, joke_type):
    """Ensure posting different options to the form returns appropriate response."""
    response = client.post('/', data=dict(category=category, lang=lang, type=joke_type))
    assert response.status_code == 200
    assert "Click the button to get a joke.." not in response.data.decode()

def test_invalid_category(client):
    """Ensure that submitting an invalid category shows an error."""
    response = client.post('/', data=dict(category='Invalid', lang='en', type='any'))
    assert "Error retrieving joke" in response.data.decode()
