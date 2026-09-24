## Introduction

This project demonstrates API testing of the public DummyJSON (https://dummyjson.com) REST API using Postman.  
It covers positive and negative scenarios, authentication flows, CRUD operations, and edge cases to practice writing assertions and organizing test collections.

## Project Overview

This project covers functional testing of the main DummyJSON endpoints:

- Authentication (Login / JWT token handling)
- Products (CRUD operations, search, filtering by category)
- Users (list, single user, search)
- Negative scenarios (non-existent resources, missing data)
- Edge cases (pagination, large skip, invalid category)

The goal is to demonstrate practical API testing skills, writing assertions, and organizing test documentation.

## Test Coverage

### Authentication
- Successful login (saves `access_token` to environment)
- Login without password
- Login with wrong password
- Get current user with token
- Get current user without token (401)

### Positive Scenarios — Products
- Get all products
- Get single product
- Search products by keyword
- Get products by category
- Add new product
- Update product (PUT)
- Delete product

### Positive Scenarios — Users
- Get all users
- Get single user
- Search users

### Negative Scenarios
- Get non-existent product (404)
- Add product without title
- Search with empty query

### Edge Cases
- Pagination with `limit` + `skip`
- Very large `skip` (empty result)
- Invalid category

## How to Run

1. Download and install [Postman](https://www.postman.com/downloads/).
2. Import the collection file:
   - `DummyJSON API Testing.postman_collection.json`
3. Create a new Environment with the following variables:

| Variable       | Value                  | Description                                     |
|----------------|------------------------|-------------------------------------------------|
| `base_url`     | `https://dummyjson.com`| Base URL of the DummyJSON API                   |
| `access_token` | _(empty)_              | Auto-filled after running "Successful Login"    |

4. Select the created Environment in the top-right corner of Postman.
5. Run the collection using **Collection Runner** or execute requests individually.
   > **Important:** Run the folder `01. Auth` first — the request *Successful Login* saves `access_token` into the environment, which is required for the protected endpoint `GET /auth/me`.

## Testing Techniques Used

- Positive / Negative testing
- Boundary and Edge cases
- Status code validation
- Response body validation (structure, types, values)
- Response time checks
- Environment variable chaining (JWT token → protected request)

## Tools

- Postman
- JavaScript (Postman Test Scripts)

## Test Execution Summary

| Metric            | Count |
|-------------------|-------|
| Requests          | 21    |
| Test Scripts      | 21    |
| Assertions        | 42    |
| Failed Assertions | 0     |

## Project Structure
DummyJSON API Testing/
├── 01. Auth/ # Login, token, /auth/me
├── 02. Products - Positive/ # CRUD + search + category
├── 03. Products - Negative/ # 404, missing title, empty search
├── 04. Users/ # List, single, search
└── 05. Edge Cases/ # Pagination, large skip, invalid category

## Notes

- DummyJSON simulates write operations (`POST`, `PUT`, `DELETE`): the server returns a successful response with a generated `id`, but the data is **not persisted** between requests. This is expected behavior of the demo API.
- Test user credentials: `emilys` / `emilyspass`.
- The `access_token` variable is set automatically by the test script in the *Successful Login* request.