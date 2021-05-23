import requests
import hashlib

from Crypto.Cipher import AES


def encrypt_padding(padding):
    r = requests.get('http://aes.cryptohack.org/ecb_oracle/encrypt/' + padding + '/')
    ciphertext = r.json()['ciphertext']
    return ciphertext # returns as hex
    

# Here is the ciphertext after prepending the input by 15 bytes (a...a) (15 a's)
# b57240c29c2a97502efaeb953fb0a45b5245173a0a15bd37034d6761ed2a7fba6397a55a1e310cbc60120becb2d9453f
if __name__ == "__main__":

    # the first 16 byte chunk of the ciphertext.
    ciphertext_0 = "b57240c29c2a97502efaeb953fb0a45b"
    # what it is prepended with.
    prepended_hex = "616161616161616161616161616161"

    # The last byte of this 16-byte ciphertext has only one unknown byte in the corresponding
    # plaintext. Namely, the last one.

    # Since it was encrypted with AES CBC, we may simply try encrypting all 255
    # possible plaintexts, and see when the corresponding ciphertext is produced.


    for i in range(0, 255):
        last_byte = bytes([i]).hex()

        candidate_plaintext = prepended_hex + last_byte

        out = encrypt_padding(candidate_plaintext)

        if(out[:32] == ciphertext_0):
            print("The last byte is %s\n", last_byte)
            print("The plaintext is : %s\n", candidate_plaintext)
            break

    # TODO : Write this code in a way that recovers the entire first block of ciphertext.











        



