from urllib.parse import urlparse
import urllib
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from marshmallow import Schema, fields
import base64
import yaml

spec = APISpec(
    title="Moto Taxi API",
    version="1.0.0",
    openapi_version="3.0.2",
    description="API for managing Moto Taxi Riders and rides",
    servers=[{"url": "http://localhost:8888"}],
    plugins=[MarshmallowPlugin()],
)

USERS = {
    "admin": {
        "password": "admin123",
        "role": "admin"
    },
    "user": {
        "password": "user123",
        "role": "user"
    },
    "demo": {
        "password": "demo123",
        "role": "user"
    },
}

spec.components.security_scheme(
    "BasicAuth",
    {
        "type": "http",
        "scheme": "basic"
    }
)

# Add API documentation for the root endpoint
spec.path(
    path="/",
    operations={
        "get": {
            "summary": "Moto Taxi API",
            "description": "Root endpoint that returns a welcome message",
            "tags": ["General"],
            "responses": {
                "200": {
                    "description": "Successful response with API welcome message",
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "message": {
                                        "type": "string",
                                        "example": "Moto Taxi API"
                                    }
                                }
                            },
                            "example": {
                                "message": "Moto Taxi API"
                            }
                        }
                    }
                }
            }
        }
    }
)

riders = [
    {"id": 1, "name": "James", "location": "Nyamirambo", "is_available": True},
    {"id": 2, "name": "Bob", "location": "Remera", "is_available": False},
    {"id": 3, "name": "Charlie", "location": "Kicukiro", "is_available": True},
    {"id": 4, "name": "David", "location": "KCC", "is_available": True},
    {"id": 5, "name": "Eve", "location": "Nyabugogo", "is_available": True},
    {"id": 6, "name": "Frank", "location": "Downtown", "is_available": False},
    {"id": 7, "name": "Graham", "location": "Kanombe", "is_available": True},
    {"id": 8, "name": "Hannah", "location": "Kimironko", "is_available": True}
]
