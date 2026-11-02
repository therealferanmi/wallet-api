import json
import urllib.error
import urllib.request


def signup(email, password):
    data = json.dumps({"email": email, "password": password}).encode()
    request = urllib.request.Request(
        "http://127.0.0.1:8000/signup",
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request) as response:
            return response.status, response.read().decode()
    except urllib.error.HTTPError as error:
        return error.code, error.read().decode()


for attempt in (1, 2):
    print(attempt, signup("ada@example.com", "MySecret123"))