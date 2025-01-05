import socket
import json

# Server details
server = "socket.cryptohack.org"
port = 13391

# Create a socket and connect to the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server, port))

# Receive the initial server message (if any)
initial_message = s.recv(4096).decode()
print("Initial Server Response:", initial_message)

# Create the message for the 'get_signature' request
request = {
    "option": "get_signature"
}

# Send the 'get_signature' request as a JSON string
s.sendall(json.dumps(request).encode() + b'\n')

# Receive the response from the server (max size of 4096 bytes)
response = s.recv(4096).decode()

# Print the response from the server
print("Server Response:", response)

# Close the socket connection
s.close()
