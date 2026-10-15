from app import app


def test_user_endpoint():
    client = app.test_client()
    response = client.get("/user?username=test")
    assert response.status_code == 200
