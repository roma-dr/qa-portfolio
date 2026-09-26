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

1. Download and install Postman.
2. Import the collection file: `DummyJSON API Testing.postman_collection.json`
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

| Metric              | Count |
|---------------------|-------|
| Requests            | 21    |
| Assertions (passed) | 42    |
| Assertions (failed) | 2     |
| Observations Noted  | 2     |

## Overview

During API testing, 2 observations were documented. These are **not defects** — 
they are noted as deviations from common REST conventions and best practices, 
with the understanding that DummyJSON is a mock/demo API that does not persist 
data or enforce business rules by design.

---

## OBS-001: Empty search query `q=` returns all products

| Field | Value |
|-------|-------|
| **ID** | OBS-001 |
| **Type** | Observation — inconsistent input handling |
| **Severity** | Informational |
| **Endpoint** | `GET /products/search?q=` |

**Steps to reproduce:**
1. Send `GET https://dummyjson.com/products/search?q=`
2. Observe response

**Expected (per common REST conventions):** `400 Bad Request` OR `200 OK` with `products: []`

**Actual:** `200 OK` with all 30 products returned (`total: 194`)

**Recommendation (for a production API):**
Return `400 Bad Request` with `{ "message": "query parameter 'q' cannot be empty" }` 
or `200 OK` with an empty array, to let clients distinguish "no results" from 
"invalid query".

---

## OBS-002: POST /products/add accepts payload without required `title`

| Field | Value |
|-------|-------|
| **ID** | OBS-002 |
| **Type** | Observation — missing server-side validation |
| **Severity** | Informational |
| **Endpoint** | `POST /products/add` |

**Steps to reproduce:**
1. Send `POST https://dummyjson.com/products/add`
2. Body: `{ "price": 99, "category": "smartphones" }` (no `title`)
3. Observe response

**Expected (per REST best practices):** `400 Bad Request` with validation error

**Actual:** `201 Created`, product returned without `title` field

**Recommendation (for a production API):**
Validate required fields on the server side and return `400 Bad Request` 
with a clear error message listing missing fields.

---

## Notes

- DummyJSON simulates write operations (`POST`, `PUT`, `DELETE`): the server returns a successful response with a generated `id`, but the data is **not persisted** between requests. This is expected behavior of the demo API.
- The `access_token` variable is set automatically by the test script in the *Successful Login* request.
