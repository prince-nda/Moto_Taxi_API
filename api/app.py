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
