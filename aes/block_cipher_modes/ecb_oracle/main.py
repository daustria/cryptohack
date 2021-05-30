import sys
import requests

# Here is the main idea of the approach.

# First we pad by 31 bytes. Our plaintext will look like this:

# AAAAAAAAAAAAAAAA AAAAAAAAAAAAAAA- ---------------- ---------------

# From the challenge, we may freely obtain the corresponding ciphertext.
# Then, for all possible bytes x, we obtain the ciphertext for

# AAAAAAAAAAAAAAAA AAAAAAAAAAAAAAAx ---------------- ---------------

# Then we compare ciphertexts of the first two blocks. If they are the same, 
# then we may assume the plaintexts were the same (this is because ECB mode is used).

# For the next round, we pad by 30 bytes. Our plaintext will look like this:

# AAAAAAAAAAAAAAAA AAAAAAAAAAAAAAc- ---------------- ---------------

# Where 'c' is the known byte of 'x' in the first round.

# for all possible bytes x, we obtain the ciphertext for 

# AAAAAAAAAAAAAAAA AAAAAAAAAAAAAAcx ---------------- ---------------

# And do the same thing as in the first round.
# We repeat this at most 32 times, since we assume the ciphertext is at most 2 blocks long.

def encrypt_padding(padding):
    r = requests.get('http://aes.cryptohack.org/ecb_oracle/encrypt/' + padding.hex() + '/')
    ciphertext = r.json()['ciphertext']
    return bytes.fromhex(ciphertext)

def make_padding(known_bytes):
    # padding + known bytes must be 31 bytes
    n = len(known_bytes)

    padding = 'A' * (31 - n)
    padding = padding.encode()
    return padding

if __name__ == "__main__":

    known_bytes = ''.encode()

    for i in range(0, 32):

        print("START ROUND %d =======================================\n" % i) 
        print("padding by %d bytes\n" % (32 - (i + 1)))
        
        # Assume the ciphertext is only 2 blocks long, so our padding only needs to be 31 bytes
        padding = make_padding(known_bytes)
        # only get the last two blocks
        padded_cipher = encrypt_padding(padding)[0:32]

        found_last_byte = 0

        # i should be searching in bytes from 0 to 255, but i know the flag is going to only have these bytes
        for j in 'qwertyuiopasdfghjklzxcvbnm1234567890_{}':

            last_byte_candidate = j.encode()

            candidate_plaintext = padding + known_bytes + last_byte_candidate

            # only get last 2 blocks
            out = encrypt_padding(candidate_plaintext)[0:32]

            # compare the first two blocks of each output.
            # if they have matching AES encryptions, then we assume their plaintexts
            # were the same.
            if (out == padded_cipher):
                found_last_byte = 1
                print("Success: the unknown byte is %s\n" % last_byte_candidate)
                known_bytes = known_bytes + last_byte_candidate
                break

        print("Known plaintext so far is %s\n" % known_bytes)
        print("END ROUND %d =========================================\n" % i) 

        if not found_last_byte:
            print("Did not find the unknown byte this round. Terminating...\n")
            sys.exit(1)

