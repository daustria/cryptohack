from Crypto.Util.number import long_to_bytes

# Takes an integer that represents a plaintext that was converted from its ascii format, and returns
# the original ascii format

# eg. the message HELLO might be converted this way, starting with ascii bytes:
# [72, 69, 76, 76, 79] -> [0x48, 0x45, 0x4c, 0x4c, 0x4f] -> 0x48454c4c4d -> 310400273487 (base 10)
def integer_to_message(n):
    byte_str = long_to_bytes(n)
    ba = bytearray(byte_str)

    message = ""

    # this byte array module could shorten the amount of code i wrote for the hex and base64 encodings...
    for i in range(0, len(ba)):
        message = message + chr(ba[i])

    return message


if __name__ == "__main__":
    # crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}
    print(integer_to_message(11515195063862318899931685488813747395775516287289682636499965282714637259206269))
