import hex_encode

_base64_chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")

# forms the number resulting from concatenating the bits of the 8-bit number b to the 8-bit number a
def _concatenate_bits(a, b):
    a = a << 8
    return a^b

def _three_bytes_to_int(a, b, c):
    res = _concatenate_bits(a,b)
    res = _concatenate_bits(res, c)
    return res

# returns the base64 expansion of the integer n in [0, 2^24) as a string
# (the range [0, 2^24) ensures any number that can be represented with 4 base64 characters)
def _base64_expansion(n):

    expansion = []

    # i am assuming the integer will not need a coefficient in the 64^4 slot in their base 64 expansion

    for i in range(3, -1, -1):
        x = n // 64**i
        n = n - x * 64**i
        expansion.append(x)

    #replace each integer in the expansion (each in [0, 64)) with the corresponding character in base64
    for i in range(0, 4):
        expansion[i] = _base64_chars[expansion[i]]

    return ''.join(expansion)

def hex_to_base64(hex_str):
    bytes_arr = hex_encode.hex_to_byte_lst(hex_str)

    #ensure the length is divisible by 3, since each iteration of our next loop converts 3 bytes to 4 characters of base64
    while(len(bytes_arr) % 3 != 0):
        bytes_arr.append(0)

    out = ""

    for i in range(0, len(bytes_arr), 3):
        # form the integer resulting from concatenating the bytes
        a = bytes_arr[i]
        b = bytes_arr[i+1]
        c = bytes_arr[i+2]
        res = _three_bytes_to_int(a, b, c)

        base64_expansion = _base64_expansion(res)
        out = out + base64_expansion

    # pad the output with = signs so the length is divisible by 3
    while(len(out) % 3 != 0):
        out = out + '='

    return out

if __name__ == "__main__":
    print(_base64_expansion(123456) == "AeJA")
    print(hex_to_base64("deadbeef"))

    # crypto/Base+64+Encoding+is+Web+Safe/
    print(hex_to_base64("72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"))
