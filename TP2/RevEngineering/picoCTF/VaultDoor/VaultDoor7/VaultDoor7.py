def int_to_hex_string(int_values):
    password_bytes = []
    for value in int_values:
        # Break the 32-bit integer into 4 bytes
        password_bytes.extend([
            (value >> 24) & 0xFF,
            (value >> 16) & 0xFF,
            (value >> 8) & 0xFF,
            value & 0xFF
        ])
    # Convert bytes to ASCII characters
    password = ''.join(chr(byte) for byte in password_bytes)
    return password

# Predefined integers
predefined = [
    1096770097, 1952395366, 1600270708, 1601398833,
    1716808014, 1734293296, 842413104, 1684157793
]

# Find the password
password = int_to_hex_string(predefined)
print(f"Decoded password: {password}")
