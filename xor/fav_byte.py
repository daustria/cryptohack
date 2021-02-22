import properties

# returns the string resulting from xor-ing the hex string s with b
def xor_with_byte(s, b):

    # two characters of hex encodes 1 byte
    # so i need to xor s with a string containing len(s)//2 bytes
    t = [b] * (len(s)//2)

    res = properties.xor_hex(s, bytes(t).hex())

    out = bytes.fromhex(res)
    return out

if __name__ == "__main__":

    s = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

    # xor s with all possible bytes
    for i in range(0, 256):
        print(xor_with_byte(s, i))



