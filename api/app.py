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

class APIHandler(BaseHTTPRequestHandler):
    def _authenticate(self):
        auth_header = self.headers.get('Authorization')
        try:
            if auth_header and auth_header.startswith('Basic '):
                encoded_credentials = auth_header.split(' ')[1]
                decoded_credentials = base64.b64decode(encoded_credentials).decode('utf-8')
                username, password = decoded_credentials.split(':', 1)
                user = USERS.get(username)
                if user and user['password'] == password:
                    return user['role']
        except Exception as e:
            print(f"Authentication error: {e}")
        return None

    def _require_auth(self, request_url: str) -> bool:  # CORRECTED: Added self parameter
        parsed_url = urlparse(request_url)
        path = parsed_url.path

        public_endpoints = ['/', '/health', '/openapi.json', '/openapi.yaml']
        return path not in public_endpoints

    def _send_auth_required(self):
        self.send_response(401)
        self.send_header('content-type', 'application/json')
        self.send_header('WWW-Authenticate', 'Basic realm="Moto Taxi API"')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(
            json.dumps({"error": "Unauthorized", "message": "Basic authentication required"}).encode('utf-8'))
