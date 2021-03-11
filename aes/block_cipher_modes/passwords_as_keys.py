import requests
import hashlib 

def get_flag():
    r = requests.get('http://aes.cryptohack.org/passwords_as_keys/encrypt_flag/')
    return r.json()['ciphertext']

def decrypt(ciphertext, password_hash):
    r = requests.get('http://aes.cryptohack.org/passwords_as_keys/decrypt/' + ciphertext + '/' + password_hash)
    return r.json()['plaintext']

if __name__ == '__main__':

    # the user is MD5 hashing a random word from word.txt
    # the length of words.txt is small enough for a brute force attack

    #edit: nevermind, brute forcing takes too long...

    flag = get_flag()

    print("flag: {}".format(flag))

    with open("words.txt") as f:

        while(1):

            word = f.readline()

            if word == '':
                break

            word = word.strip()

            possible_key = hashlib.md5(word.encode()).digest().hex()

            plaintext = decrypt(flag, possible_key)

            plaintext = bytes.fromhex(plaintext)

            print(plaintext)

            if plaintext[:6] == b'crypto':
                print("possible key word : {}".format(word))
                print("possible password_hash : {}".format(possible_key))

