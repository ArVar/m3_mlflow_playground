import requests

response = requests.get(
    "http://localhost:5000/",
    auth=("admin", "password"),
)
print(response.text)
