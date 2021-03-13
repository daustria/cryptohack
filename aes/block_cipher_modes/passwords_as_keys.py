import requests
import hashlib 
from Crypto.Cipher import AES


def get_flag():
    r = requests.get('http://aes.cryptohack.org/passwords_as_keys/encrypt_flag/')
    return r.json()['ciphertext']

def decrypt(ciphertext, password_hash):
    r = requests.get('http://aes.cryptohack.org/passwords_as_keys/decrypt/' + ciphertext + '/' + password_hash)
    return r.json()['plaintext']

def decrypt_offline(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = bytes.fromhex(password_hash)

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return decrypted


if __name__ == '__main__':


    flag = get_flag()

    # the encrypted flag is 64 bytes, the key is 32 bytes long. so there are two blocks in the AES encryption.
    # since the mode is ECB, i only need to decrypt the first block
    # and meaningful plaintext will appear (if the key is right)
    flag = flag[0:32]

    print("flag: {}".format(flag))

    with open("words.txt") as f:

        while(1):

            word = f.readline()

            if word == '':
                break

            word = word.strip()

            possible_key = hashlib.md5(word.encode()).digest().hex()

            plaintext = decrypt_offline(flag, possible_key)
            print(plaintext)

            if plaintext[:6] == b'crypto':
                print("possible key word : {}".format(word))
                print("possible password_hash : {}".format(possible_key))

