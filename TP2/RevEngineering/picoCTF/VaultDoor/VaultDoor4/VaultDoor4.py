def generate_password():
    # myBytes array equivalent in Python (converting the Java byte values)
    myBytes = [
        106, 85, 53, 116, 95, 52, 95, 98,
        0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
        0o142, 0o131, 0o164, 0o63, 0o163, 0o137, 0o143, 0o61,
        ord('9'), ord('4'), ord('f'), ord('7'),
        ord('4'), ord('5'), ord('8'), ord('e')
    ]

    # Convert byte values to characters
    password = ''.join(chr(byte) for byte in myBytes)
    return password

# Generate and print the password
password = generate_password()
print(f"Generated password: {password}")
