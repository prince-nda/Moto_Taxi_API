# Moto_Taxi_API

This document explains **how the Moto Taxi API functions**, its flow, authentication model, and how requests are handled from start to response.

---

## Overview

The Moto Taxi API is a simple REST-style service that allows clients to:

* View registered moto taxi riders
* Check which riders are available
* Retrieve rider details by ID
* Access API documentation

The API is built using Python’s built-in HTTP server and operates entirely in-memory.

---

## Server Startup Flow

1. The server starts on `localhost:8888`
2. An HTTP server listens for incoming requests
3. Each request is handled by the `APIHandler` class
4. Requests are routed based on **URL path** and **HTTP method**

---

## Authentication Flow (Basic Auth)

The API uses **HTTP Basic Authentication** for protected endpoints.

### How authentication works:

1. Client sends a request with an `Authorization` header
2. Credentials are Base64-decoded (`username:password`)
3. Credentials are checked against the in-memory `USERS` dictionary
4. If valid → request continues
5. If invalid or missing → API returns **401 Unauthorized**

### Public vs Protected Endpoints

| Type      | Description                |
| --------- | -------------------------- |
| Public    | No authentication required |
| Protected | Authentication required    |

Public endpoints:

* `/`
* `/health`
* `/openapi.json`
* `/openapi.yaml`

All other endpoints require authentication.

---

## Rider Data Handling

Riders are stored in an **in-memory list**:

* Each rider has an `id`, `name`, `location`, and `is_available` flag
* No database is used
* Data resets when the server restarts

### Example Rider Object

```json
{
  "id": 1,
  "name": "James",
  "location": "Nyamirambo",
  "is_available": true
}
```

---

## Request Routing Logic

When a GET request arrives:

1. The URL path is parsed
2. Authentication is checked (if required)
3. The request is routed to the correct handler
4. A JSON response is returned with an HTTP status code

### Routing Examples

* `/riders` → returns all riders
* `/riders/available` → filters only available riders
* `/riders/{id}` → returns a specific rider

If a rider ID does not exist, the API returns **404 Not Found**.

---

## API Documentation (OpenAPI)

The API automatically exposes its documentation using **OpenAPI 3.0**.

* `/openapi.json` → JSON format
* `/openapi.yaml` → YAML format

These specs can be imported into tools like **Postman** or **Swagger UI**.

---

## CORS Support

The API supports Cross-Origin Resource Sharing (CORS):

* Handles `OPTIONS` requests
* Allows all origins (`*`)
* Supports common HTTP methods

This makes the API usable from browsers and frontend applications.

---

## Health Check

The `/health` endpoint allows monitoring tools or load balancers to confirm that:

* The server is running
* The API is responsive

Response example:

```json
{ "status": "OK" }
```

---

## Limitations

* No persistent storage
* No ride booking logic
* No role-based permissions
* Not production-ready (learning-focused)

---


## Summary

The Moto Taxi API demonstrates:

* Core REST concepts
* Authentication handling
* Request routing
* API documentation
* Clean separation of concerns

It is ideal for **learning backend fundamentals**, **API security basics**, and **documentation practices**.

---

**Author:** Prince Ndahiro
Software Engineering Student
