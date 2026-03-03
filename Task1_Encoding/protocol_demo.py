import requests

response = requests.get("https://example.com")
print("Status Code:", response.status_code)
print("Protocol Used:", response.url)
