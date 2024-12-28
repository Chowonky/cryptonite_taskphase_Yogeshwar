```
 public boolean checkPassword(String password) {
        byte[] passBytes = password.getBytes();
        byte[] myBytes = {
            106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
            0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
            0142, 0131, 0164, 063 , 0163, 0137, 0143, 061 ,
            '9' , '4' , 'f' , '7' , '4' , '5' , '8' , 'e' ,
        };
        for (int i=0; i<32; i++) {
            if (passBytes[i] != myBytes[i]) {
                return false;
            }
        }
        return true;
    }
```
- Here we need to create a password such that when it is converted to `bytes`, the resulting `passwordBytes` array should be exactly equal to `myBYtes` array
- `VaultDoor4.py` python code to extract the password
```
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

```
![alt text](<Screenshot from 2024-12-27 15-55-12.png>)
- Flag is picoCTF{jU5t_4_bUnCh_0f_bYt3s_c194f7458e}