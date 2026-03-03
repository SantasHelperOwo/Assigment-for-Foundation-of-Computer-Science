data = "Hello Noob!"
encoded = data.encode("utf-8").hex()
print("Hex Encoded:", encoded)

decoded = bytes.fromhex(encoded).decode("utf-8")
print("Decoded:", decoded)
