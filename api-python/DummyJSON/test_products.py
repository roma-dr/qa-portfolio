import requests

BASE_URL = "https://dummyjson.com"

def test_get_all_products():
    response = requests.get(f"{BASE_URL}/products")

    assert response.status_code == 200
    data = response.json()
    assert "products" in data
    assert isinstance(data["products"], list)
    assert "total" in data

def test_get_single_product():
    response = requests.get(f"{BASE_URL}/products/1")

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "title" in data
    assert "price" in data

def test_get_nonexistent_product():
    response = requests.get(f"{BASE_URL}/products/9999")

    assert response.status_code == 404
    data = response.json()
    assert "message" in data

def test_search_products():
    response = requests.get(f"{BASE_URL}/products/search", params={"q": "phone"})

    assert response.status_code == 200
    data = response.json()
    assert "products" in data
    assert isinstance(data["products"], list)

def test_add_product():
    payload = {
        "title": "Test Product QA",
        "price": 99,
        "category": "smartphones"
    }

    response = requests.post(f"{BASE_URL}/products/add", json=payload)

    assert response.status_code in [200, 201]
    data = response.json()
    assert "id" in data
    assert data["title"] == "Test Product QA"

def test_update_product():
    payload = {
        "title": "Updated Product Title"
    }

    response = requests.put(f"{BASE_URL}/products/1", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Product Title"

def test_delete_product():
    response = requests.delete(f"{BASE_URL}/products/1")

    assert response.status_code == 200
    data = response.json()
    assert "id" in data