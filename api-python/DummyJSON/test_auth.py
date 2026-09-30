import requests

BASE_URL = "https://dummyjson.com"

def test_successful_login():
    url = f"{BASE_URL}/auth/login"
    payload = {
        "username": "emilys",
        "password": "emilyspass",
        "expiresInMins": 30
    }

    response = requests.post(url, json=payload)

    assert response.status_code == 200
    data = response.json()
    assert "accessToken" in data
    assert data["accessToken"]
    assert isinstance(data["accessToken"], str)

def test_login_without_password():
    url = f"{BASE_URL}/auth/login"
    payload = {
        "username": "emilys"
    }

    response = requests.post(url, json=payload)

    assert response.status_code == 400
    data = response.json()
    assert "message" in data

def test_login_with_wrong_password():
    url = f"{BASE_URL}/auth/login"
    payload = {
        "username": "emilys",
        "password": "wrongpassword"
    }

    response = requests.post(url, json=payload)

    assert response.status_code == 400
    data = response.json()
    assert "message" in data

def test_get_current_user_without_token():
    url = f"{BASE_URL}/auth/me"

    response = requests.get(url)

    assert response.status_code == 401
    data = response.json()
    assert "message" in data

def test_get_current_user_with_token():
    login_url = f"{BASE_URL}/auth/login"
    payload = {
        "username": "emilys",
        "password": "emilyspass"
    }
    login_response = requests.post(login_url, json=payload)
    token = login_response.json()["accessToken"]

    url = f"{BASE_URL}/auth/me"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)

    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "username" in data
    assert "email" in data