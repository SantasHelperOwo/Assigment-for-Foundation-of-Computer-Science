import urllib.parse

data = "Hello Noob! This is URL demo."
encoded = urllib.parse.quote(data)
print("URL Encoded:", encoded)

decoded = urllib.parse.unquote(encoded)
print("Decoded:", decoded)
