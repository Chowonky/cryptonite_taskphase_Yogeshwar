#!/usr/bin/env python
from pwn import remote
import string

host = 'mercury.picoctf.net'
port = 50075

io = remote(host, port)
io.timeout=1000

io.recvuntil("flag: ")
encrypted_flag = io.recvuntil("\nn: ").decode().strip()
n = io.recvuntil("\ne: ").decode().strip() 
e = io.recvuntil("\n").decode().strip()     

def remove_segments(result, segments):
    # Remove all previously seen segments.
    for segment in segments:
        result = result.replace(segment, "")
    return result

known_segments = []
decrypted_flag = "" 
while "}" not in decrypted_flag:
    for c in string.ascii_lowercase + string.digits + "{}_CTF": # Characters normally present in picoCTF flag
        current_test = decrypted_flag + c
        io.sendlineafter("I will encrypt whatever you give me: ", current_test)
        current_encrypt_test = io.recvuntil("\n").decode().strip()
        current_encrypt_test = current_encrypt_test.replace("Here you go: ", "")

        current_char_rep = remove_segments(current_encrypt_test, known_segments)

        if current_char_rep in encrypted_flag:
            print("%s%s" % (decrypted_flag, c))
            decrypted_flag += c
            known_segments.append(current_char_rep)
            break

print("Complete Flag: %s" % decrypted_flag)