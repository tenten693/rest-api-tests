import requests  # ← обязательно!
import pytest

def test_invalid_login():
    headers = {"x-api-key": "reqres-free-v1"}
    response = requests.post("https://reqres.in/api/login", json={"email": "test@test"}, headers=headers)
    assert response.status_code == 400
    assert "error" in response.json()

def test_not_found():
    headers = {"x-api-key": "reqres-free-v1"}
    response = requests.get("https://reqres.in/api/users/999", headers=headers)
    assert response.status_code == 404

