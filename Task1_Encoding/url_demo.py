import http.client

conn = http.client.HTTPSConnection("example.com")
conn.request("GET", "/")
response = conn.getresponse()
print("Status:", response.status)
print("Protocol: HTTPS")
