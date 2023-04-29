import requests

url = "http://localhost:5000/versions"
data = {
    "versions": ["2.5.0-dev.1", "2.4.2-5354", "2.4.2-test.675", "2.4.1-integration.1"]
}

response = requests.post(url, json=data)
print(response.json())

input("Press Enter to exit...")