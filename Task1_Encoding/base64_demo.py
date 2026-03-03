import base64

data = "Hello Noob, this is Base64 demo!"
encoded = base64.b64encode(data.encode("utf-8"))
print("Encoded:", encoded.decode("utf-8"))

decoded = base64.b64decode(encoded).decode("utf-8")
print("Decoded:", decoded)
