import properties 

# challenge is to recover the flag from the encrypted (by one time pad) hex string 
# 0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104

# the flag in the challenge has the format crypto{FLAG} so I can recover some of the plaintext bytes

ctext = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

if __name__ == "__main__":
    
    ptext_0 = "crypto{1".encode().hex()
    key_0 = properties.xor_hex(ctext[0:len(ptext_0)], ptext_0)

    # key corresponding to the part that encrypts the bytes corresponding to the plaintext portion ptext_0
    # it prints: b'myXORke'
    print(bytes.fromhex(key_0))


    # i know 'myXORkey' part of the key, need to guess the second part
    key_1 = ("myXORkey").encode().hex()

    ptext_1 = properties.xor_hex(ctext[0:len(key_1)], key_1)

    # shows some of the plaintext corresponding to the part that is encrypted by key_1
    print(bytes.fromhex(ptext_1))


    # this shows the last letter of the key is 'y'
    # ptext_2 = "}".encode().hex()
    # ctext_2 = "04"

    # res = properties.xor_hex(ptext_2, ctext_2)
    # print(bytes.fromhex(res))

    
