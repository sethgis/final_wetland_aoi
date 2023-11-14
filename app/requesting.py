import requests

data = {
    "wetland": {"name": "Barotse"},
    "indicator": {"name": "LULC"}
}

response = requests.post("http://localhost:8080/", json=data)
print(response.status_code)
print(response.json())