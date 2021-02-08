import main
from cache import redis

import pytest
import json

@pytest.fixture
def client():
    with main.app.test_client() as client:
        yield client

def test_home_endpoint(client):
    """Dummy test for '/' endpoint"""

    response = client.get('/')
    assert b'droids' in response.data

def test_cache(client):
    """Test caching"""

    redis.flushall()
    response = client.get('/films')
    cached_response = client.get('/films')
    assert response.data == cached_response.data

def test_films(client):
    """Test films endpoint"""

    response = client.get('/films')
    film_data = json.loads(response.data)
    assert len(film_data) == 6
    assert all('id' in f and 'title' in f and 'release_date' in f for f in film_data)

def test_characters(client):
    """Test characters endpoint"""

    for film_id in range(0, 6):
        response = client.post(
            '/characters',
            data=json.dumps({'film_id': film_id}),
            headers={"Content-Type": "application/json"})
        character_data = json.loads(response.data)
        assert any(c['name'] == 'R2-D2' for c in character_data)
        assert any(c['name'] == 'C-3PO' for c in character_data)
