from fastapi.testclient import TestClient

from project_name.app.main import app

client = TestClient(app)


def test_hello_world():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello world"}
