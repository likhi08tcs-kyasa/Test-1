
from app import app


def test_user_endpoint():
    client = app.test_client()
    response = client.get("/user?username=test")
    assert response.status_code == 200


def test_sql_injection_input_is_treated_as_data():
    client = app.test_client()
    response = client.get(
        "/user",
        query_string={"username": "' OR '1'='1"}
    )

    assert response.status_code == 200
    assert response.get_data(as_text=True) == "[]"
