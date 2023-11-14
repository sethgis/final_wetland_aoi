import requests

data = {
    "wetland": {"name": "Barotse"},
    "indicator": {"name": "LULC"}
}

response = requests.post("http://66.42.65.87:8000/generate_sld/", json=data)
print(response.status_code)
print(response.json())
