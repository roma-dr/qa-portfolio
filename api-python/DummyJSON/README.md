# DummyJSON API Autotests

API autotests for [DummyJSON](https://dummyjson.com) using Python, `requests` and `pytest`.

## Overview

This project demonstrates basic API test automation:
- Authentication (login, JWT token)
- Products (CRUD, search, negative cases)
- Users (list, single user, search)

## Test Coverage

### Auth (5 tests)
- Successful login
- Login without password
- Login with wrong password
- Get current user with token
- Get current user without token (401)

### Products (7 tests)
- Get all products
- Get single product
- Get non-existent product (404)
- Search products
- Add product
- Update product
- Delete product

### Users (3 tests)
- Get all users
- Get single user
- Search users

**Total: 15 tests**

## Setup

```bash
python -m venv .venv
source .venv/bin/activate      # macOS / Linux
pip install -r requirements.txt
```

## Run

```bash
pytest -v
```
