## Introduction

This project demonstrates API testing of the public ReqRes(https://reqres.in) REST API using Postman.  
It covers positive and negative scenarios, authentication flows, and edge cases to practice writing assertions and organizing test collections.

## Project Overview

This project covers functional testing of the main ReqRes endpoints:

- User management (CRUD operations)
- Authentication (Login / Register)
- Negative scenarios
- Edge cases (delays, pagination, non-existent resources)

The goal is to demonstrate practical API testing skills, writing assertions, and organizing test documentation.

## Test Coverage

### Positive Scenarios
- Get list of users
- Get single user
- Create user
- Update user (PUT)
- Update user (PATCH)
- Delete user

### Negative Scenarios
- Get non-existent user
- Create user without body
- Create user with empty name

### Authentication
- Successful login
- Login without password
- Successful registration
- Register without password

### Edge Cases
- Delayed response
- List users with per_page
- Very large page number
- User not found

## How to Run

1. Download and install [Postman](https://www.postman.com/downloads/).
2. Import the collection file: `postman/ReqRes_API_Testing.postman_collection.json`
3. Create a new Environment with the following variables:

| Variable   | Value                 | Description                          |
|------------|-----------------------|--------------------------------------|
| `base_url` | `https://reqres.in`   | Base URL of the API                  |
| `api_key`  | `your_api_key_here`   | API key from [app.reqres.in](https://app.reqres.in) |

4. Select the created Environment in the top-right corner of Postman.
5. Run the collection using **Collection Runner** or execute requests individually.


## Testing Techniques Used

- Positive / Negative testing
- Boundary and Edge cases
- Status code validation
- Response body validation
- Response time checks

## Tools

- Postman
- JavaScript (Postman Test Scripts)

## Test Execution Summary

| Metric            | Count |
|-------------------|-------|
| Requests          | 17    |
| Test Scripts      | 17    |
| Assertions        | 37    |
| Failed Assertions | 0     |
