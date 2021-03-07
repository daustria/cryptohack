import requests
import hashlib 

def get_flag():
    r = requests.get('http://aes.cryptohack.org/passwords_as_keys/encrypt_flag/')
    return r.json()['ciphertext']

if __name__ == '__main__':

    # the user is MD5 hashing a random word from word.txt
    # the length is small enough to simply hash all the words myself and check for matching ciphertexts..


    with open("words.txt") as f:
        words = [w.strip() for w in f.readlines()]
    passwords = [hashlib.md5(w.encode()).digest() for w in words]

    flag = get_flag()
    # flag starts with 'crypto{' and ends with '}'
    flag = flag[14:-2]

    print("flag: {}".format(flag))
    for w in words:

        # after i narrow down possible passwords, im hoping i can do some non-automated work to
        # get the result...
        password_hash = hashlib.md5(w.encode()).digest().hex()
        print(password_hash)

        if flag[:len(password_hash)] == password_hash:
            print("Possible password: {} , Hash : {}".format(w, password_hash))

