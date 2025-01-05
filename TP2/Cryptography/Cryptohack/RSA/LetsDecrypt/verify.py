import socket
import json
from Crypto.Util.number import bytes_to_long
from pkcs1 import emsa_pkcs1_v15

def connect_to_server(server, port):
    conn = socket.create_connection((server, port))
    return conn

def send_and_receive(conn, data):
    conn.sendall(json.dumps(data).encode() + b"\n")
    response = b""
    while not response.endswith(b"\n"):
        response += conn.recv(1024)
    return json.loads(response.decode())

server = 'socket.cryptohack.org'
PORT = 13391

conn = connect_to_server(server, PORT)
print(conn.recv(1024).decode())

data = {"option": "get_signature"}
response = send_and_receive(conn, data)

SIGNATURE = int(response['signature'], 16)
SERVER_N = int(response['N'], 16)
SERVER_E = int(response['e'], 16)

print(f"Received SIGNATURE: {hex(SIGNATURE)}")
print(f"Received N: {hex(SERVER_N)}")
print(f"Received e: {hex(SERVER_E)}")

msg = "I am Mallory and I own CryptoHack.org"

digest = emsa_pkcs1_v15.encode(msg.encode(), 256)
digest_long = bytes_to_long(digest)

e = 1
n = SIGNATURE - digest_long

if n <= 0:
    raise ValueError("Computed n is not positive.")

print(f"Computed n: {hex(n)}")
print(f"Using e: {hex(e)}")

data = {
    "option": "verify",
    "msg": msg,
    "N": hex(n),
    "e": hex(e)
}

response = send_and_receive(conn, data)

if 'msg' in response:
    print(response['msg'])
else:
    print(f"Error: {response.get('error', 'Unknown error')}")

conn.close()
