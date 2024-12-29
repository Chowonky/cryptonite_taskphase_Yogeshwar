from pwn import remote
import json
import hashlib
from Crypto.Cipher import AES
from sympy.ntheory import discrete_log

# Connect to the server
HOST = 'socket.cryptohack.org'
PORT = 13379
conn = remote(HOST, PORT)

# Function to receive JSON data from the server
def recv_json():
    line = conn.recvline()  # Read a line from the server
    return json.loads(line.decode())  # Decode and load the JSON data

# Function to send JSON data after waiting for the prompt
def send_json(data):
    request = json.dumps(data).encode()  # Convert the data to JSON and encode it
    conn.sendlineafter(": ", request)  # Send the data after the prompt ": "

# Intercept Alice's initial message
conn.readuntil(": ")
alice = recv_json()
print("Intercepted from Alice:", alice)

# Modify Alice's supported algorithms to only include 'DH64' and send to Bob
alice['supported'] = ["DH64"]
print("Send to Bob:", alice)
send_json(alice)

# Intercept Bob's response containing his chosen algorithm
conn.readuntil(": ")
bob = recv_json()
print("Received from Bob:", bob)

# Forward Bob's chosen algorithm back to Alice
print("Send to Alice:", bob)
send_json(bob)

# Intercept Alice's Diffie-Hellman parameters (p, g, A)
conn.readuntil(": ")
alice = recv_json()
print("Captured Alice's response (p, g, A):", alice)
p = int(alice['p'], 16)
g = int(alice['g'], 16)
A = int(alice['A'], 16)

# Intercept Bob's Diffie-Hellman response (B)
conn.readuntil(": ")
bob = recv_json()
print("Received from Bob (B):", bob)
B = int(bob['B'], 16)

# Intercept the encrypted message sent by Alice
conn.readuntil(": ")
encrypted = recv_json()
print("Captured Alice's encrypted message:", encrypted)

# Brute-force to find the private key 'a' (Alice's private key)
a = discrete_log(p, A, g)

# Compute the shared secret
shared_secret = pow(B, a, p)

# Derive the AES key from the shared secret
sha1 = hashlib.sha1()
sha1.update(str(shared_secret).encode('ascii'))
key = sha1.digest()[:16]

# Decrypt the flag using AES
iv = bytes.fromhex(encrypted['iv'])
ciphertext = bytes.fromhex(encrypted['encrypted_flag'])
cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = cipher.decrypt(ciphertext)
flag = plaintext.decode('utf-8').strip()  # Strip padding

print("Flag:", flag)

# Close the connection
conn.close()
    