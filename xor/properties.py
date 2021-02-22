k1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
k1_xor_k2 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
k2_xor_k3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
flag_xor_k1_k2_k3 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

# to obtain the flag, i need to xor the last string with k1^k2^k3

# xor_hex(s,t): returns the hex string corresponding to the
# byte-wise xor of the hex strings s,t
def xor_hex(s, t):
    b1 = bytearray.fromhex(s)
    b2 = bytearray.fromhex(t)

    n = len(b1)
    m = len(b2)
    
    res = [0]*max(n,m)

    for i in range(0, max(n,m)):

        if i >= n:
            res[i] = b2[i]
        elif i >= m:
            res[i] = b1[i]
        else:
            res[i] = b1[i]^b2[i]

    byte_str = bytes(res)
    return byte_str.hex()

if __name__ == "__main__":
    xor_k1_k2_k3 = xor_hex(k1, k2_xor_k3)
    flag = xor_hex(xor_k1_k2_k3, flag_xor_k1_k2_k3)
    # prints the hex string corresponding to a string like crypto{xor_is_assoc1ativ3} or something,
    # giving me the flag of the challenge
    print(flag)

    
