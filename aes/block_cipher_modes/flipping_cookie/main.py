import requests

def xor_bytes(s, t):
    return bytes([a ^ b for a,b in zip(s,t)])

def get_cookie():
    r = requests.get('http://aes.cryptohack.org/flipping_cookie/get_cookie')
    out = r.json()['cookie']
    iv = bytes.fromhex(out[0:32])
    cookie = bytes.fromhex(out[32:])

    return (iv, cookie)

def check_admin(cookie, iv):
    r = requests.get('http://aes.cryptohack.org/flipping_cookie/check_admin/'+cookie+'/'+iv)
    return r.json()

if __name__ == "__main__":

    out = get_cookie()
    iv = out[0]
    cookie = out[1]

    # first blocks of the true plaintext
    plaintext_0 = "admin=False;expi".encode()

    # Upon decrypting cookie_0 in CBC, we get plain_0 XOR'd with iv. 
    # Call this result q.
    # q is then XOR'd with the iv to obtain the original plaintext.

    # In this challenge, we may choose the iv that is used for decrypting, so 
    # I can choose a malicious IV such that q XOR IV contains 'admin=True;'

    malicious_cookie = "admin=True;xxxxx".encode()

    # This is what the server gets when the first block is decrypted in CBC mode
    resulting_decryption = xor_bytes(plaintext_0, iv)

    malicious_iv = xor_bytes(resulting_decryption, malicious_cookie)

    print(check_admin(cookie.hex(), malicious_iv.hex()))
