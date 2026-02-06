import requests
import json

BASE_URL = "http://localhost:8888"


def test_endpoint(method="GET", endpoint="", auth=None, data=None):
    """Test an endpoint"""
    url = f"{BASE_URL}{endpoint}"
    try:
        if method == "GET":
            if auth:
                response = requests.get(url, auth=auth)
            else:
                response = requests.get(url)
        else:
            response = requests.request(method, url, auth=auth, json=data)

        print(f"\n{'=' * 60}")
        print(f"Testing: {method} {endpoint}")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text[:200]}")
        return response
    except Exception as e:
        print(f"Error: {e}")
        return None


# Run tests
if __name__ == "__main__":
    print("Testing Moto Taxi API...")

    # Test 1: Root endpoint (no auth)
    test_endpoint("GET", "/")

    # Test 2: Health (no auth)
    test_endpoint("GET", "/health")

    # Test 3: OpenAPI JSON (no auth)
    test_endpoint("GET", "/openapi.json")

    # Test 4: Riders without auth (should fail)
    test_endpoint("GET", "/riders")

    # Test 5: Riders with auth (should work)
    test_endpoint("GET", "/riders", auth=("admin", "admin123"))

    # Test 6: Available riders
    test_endpoint("GET", "/riders/available", auth=("user", "user123"))

    # Test 7: Specific rider
    test_endpoint("GET", "/riders/1", auth=("demo", "demo123"))

    # Test 8: Non-existent rider
    test_endpoint("GET", "/riders/999", auth=("admin", "admin123"))
