from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_delete_signup_removes_participant():
    response = client.delete("/activities/Chess%20Club/signup?email=michael@mergington.edu")

    assert response.status_code == 200
    assert response.json()["message"] == "Unregistered michael@mergington.edu from Chess Club"

    activities = client.get("/activities").json()
    assert "michael@mergington.edu" not in activities["Chess Club"]["participants"]

    client.post("/activities/Chess%20Club/signup?email=michael@mergington.edu")


def test_delete_signup_missing_email_returns_404():
    response = client.delete("/activities/Chess%20Club/signup?email=missing@mergington.edu")

    assert response.status_code == 404
    assert response.json()["detail"] == "Student not found in this activity"
