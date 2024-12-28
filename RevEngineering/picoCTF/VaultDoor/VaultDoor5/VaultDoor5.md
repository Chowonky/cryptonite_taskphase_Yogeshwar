```
    public String base64Encode(byte[] input) {
        return Base64.getEncoder().encodeToString(input);
    }

    public String urlEncode(byte[] input) {
        StringBuffer buf = new StringBuffer();
        for (int i=0; i<input.length; i++) {
            buf.append(String.format("%%%2x", input[i]));
        }
        return buf.toString();
    }

    public boolean checkPassword(String password) {
        String urlEncoded = urlEncode(password.getBytes());
        String base64Encoded = base64Encode(urlEncoded.getBytes());
        String expected = "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVm"
                        + "JTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2"
                        + "JTM0JTVmJTY1JTMzJTMxJTM1JTMyJTYyJTY2JTM0";
        return base64Encoded.equals(expected);
    }
```
- Here we need to create a password such that when it is `urlEncoded` and then `base64Encoded` it should match the `base64Encoding` of `expected` string,
- base64encoded(password)=expected
- decoding the base64encoded(password) we get the urlEncoded(password)
- further decoding the urlEncoded(password) we get the password
- using [Base64Decoder](https://www.base64decode.org/) and [URLDecoder](https://meyerweb.com/eric/tools/dencoder/) we get the password "c0nv3rt1ng_fr0m_ba5e_64_e3152bf4"
- Flag is picoCTF{c0nv3rt1ng_fr0m_ba5e_64_e3152bf4}