import requests

BASE_URL = "https://dummyjson.com"

def test_get_all_users():
    response = requests.get(f"{BASE_URL}/users")

    assert response.status_code == 200
    data = response.json()
    assert "users" in data
    assert isinstance(data["users"], list)
    assert len(data["users"]) > 0

def test_get_single_user():
    response = requests.get(f"{BASE_URL}/users/1")

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "firstName" in data
    assert "email" in data

def test_search_users():
    response = requests.get(f"{BASE_URL}/users/search", params={"q": "John"})

    assert response.status_code == 200
    data = response.json()
    assert "users" in data
    assert isinstance(data["users"], list)