import os
import tempfile
import pytest
from app import app


@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])


def test_like_feature(client):
    # Path to the liked_jokes.txt file
    liked_jokes_path = 'liked_jokes.txt'

    # Clean state: Ensure the liked_jokes.txt is empty or set to a known state before testing
    open(liked_jokes_path, 'w').close()

    # The joke to be liked
    test_joke = "Why did the computer go to the doctor? Because it had a virus!"

    # Simulate liking the joke by making a POST request with the necessary form data
    client.post('/', data={'like': 'true', 'joke': test_joke})

    # Verify the joke was appended to liked_jokes.txt
    with open(liked_jokes_path, 'r') as file:
        file_contents = file.read()

    assert test_joke in file_contents, "The joke was not found in liked_jokes.txt"

