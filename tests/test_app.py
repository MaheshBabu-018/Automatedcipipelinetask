from src.app import app
import pytest

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_root(client):
    resp = client.get('/')
    assert resp.status_code == 200
    assert resp.get_json() == {"message": "Hello from Flask CI!"}
