# OpenWeatherMap API Testing

API testing project for the public [OpenWeatherMap](https://openweathermap.org/api) Current Weather and Forecast API using Postman.

## Overview

This project covers functional testing of a real public weather API:
- Current weather by city, country and coordinates
- Units (metric / imperial) and language parameters
- 5-day forecast
- Negative scenarios (missing/invalid API key, invalid city, invalid coordinates)
- Edge cases (special characters, response time)

## Test Coverage

### Positive — Current Weather
- Weather by city name
- Weather by city + country
- Weather by coordinates
- Units: metric
- Units: imperial
- Language: Russian

### Positive — Forecast
- 5-day forecast by city

### Negative
- Missing API key (401)
- Invalid API key (401)
- Non-existent city (404)
- Empty city parameter
- Invalid coordinates
- Missing location parameter

### Edge Cases
- Special characters in city name
- Response time under 3000ms

## How to Run

1. Install [Postman](https://www.postman.com/downloads/).
2. Import the collection:
   - `OpenWeatherMap API Testing.postman_collection.json`
3. Create an Environment with these variables:

| Variable   | Example value                                      | Description                |
|------------|----------------------------------------------------|----------------------------|
| `base_url` | `https://api.openweathermap.org/data/2.5`          | API base URL               |
| `api_key`  | `your_openweathermap_api_key`                      | Free API key from website  |
| `city`     | `London`                                           | Default city for requests  |

4. Get a free API key: [https://openweathermap.org/api](https://openweathermap.org/api)  
5. Select the Environment.
6. Run the collection via Collection Runner or send requests one by one.

## Testing Techniques Used

- Positive / Negative testing
- Boundary and edge cases
- Status code validation
- Response body validation
- Response time checks
- Environment variables for base URL and API key

## Tools

- Postman
- JavaScript (Postman Test Scripts)

## Notes

- This is a real production API, not a mock service.
- Classic functional bugs are unlikely. The value of this project is practice with a live API, API keys, and negative scenarios.
