import sys
import requests
import hashlib

# This file is copied over from the one deciphering only the first block of ciphertext.
# From running the first file, I know that the ciphertext of the first block is :
# 63727970746f7b70336e3675316e355f
# crypto{p3n6u1n5_

# From running this file, the ciphertext in the second block is :
# h473_3cb}

# We modify the code slightly, so that it deciphers the second block of ciphertext

def encrypt_padding(padding):
    r = requests.get('http://aes.cryptohack.org/ecb_oracle/encrypt/' + padding + '/')
    ciphertext = r.json()['ciphertext']
    return ciphertext # returns as hex    

if __name__ == "__main__":

    # The plaintext of the first block
    plaintext_0 = "63727970746f7b70336e3675316e355f"

    # The 15 bytes to pad the plaintext initially
    initial_padding = "616161616161616161616161616161" 

    # The block of the ciphertext corresponding to the unpadded section.
    unpadded_ciphertext = encrypt_padding(initial_padding + "61")[64:96]

    # The bytes of the unpadded plaintext known so far
    known_bytes = ""

    for j in range(0,16):

        print("START ROUND %d\n" % j)

        # trim the prepend input, so the plaintext includes all the known bytes
        # The original prepend hex is 61....61 up until known bytes appear.

        padding = initial_padding
        if(j != 0):
            padding = initial_padding[:-(2*j)]

        # this goes out of bounds on round j = 15, which is okay since it just becomes empty
        known_plaintext = plaintext_0[2*(j+1):]

        print("padding by %d bytes\n" % (len(padding) / 2))
        print("known plaintext of the second block, after padding, is : %s\n" % (known_plaintext + known_bytes))

        ciphertext = ""

        if(padding == ""):
            ciphertext = unpadded_ciphertext
        else:
            ciphertext = encrypt_padding(padding)[32:64]

        print("padded ciphertext is %s\n" % ciphertext)

        # The last byte of this 16-byte ciphertext has only one unknown byte in the corresponding
        # plaintext. Namely, the last one.
    
        # Since it was encrypted with AES CBC, we may simply try encrypting all 255
        # possible plaintexts, and see when the corresponding ciphertext is produced. 

        found_byte = 0 

        for i in range(0, 255):

            last_byte = bytes([i]).hex()
            

            candidate_plaintext = known_plaintext + known_bytes + last_byte

            out = encrypt_padding(candidate_plaintext)[0:32]

    
            if(out == ciphertext):

                found_byte = 1

                print("END ROUND %d \n" % j)
                print("The unknown byte is %s\n" % last_byte)

                known_bytes = known_bytes + last_byte
                break

        print("The known plaintext is: %s\n" % known_bytes)

        if not found_byte:
            print("Did not find the unknown byte... terminating\n")
            sys.exit(1)



