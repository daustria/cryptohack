import sys

hex_letters = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f']
digits = ['0','1','2','3','4','5','6','7','8','9']

# returns the integer corresponding to the two digit hex value ab
def _two_hex_to_byte(a, b):
    tens = hex_letters.index(a)
    ones = hex_letters.index(b)

    return (tens * 16) + (ones * 1)


def bytes_to_str(byte_arr):

    for i in range(0, len(byte_arr)):
        byte_arr[i] = chr(byte_arr[i])
    return ''.join(byte_arr)

def hex_to_byte_lst(hex_str):
    hex_copy = list(hex_str)
    n = len(hex_copy)

    if n % 2 == 1:
        hex_copy.append('0')
        n += 1

    byte_arr = []

    for i in range(0, n, 2):
        a = hex_copy[i]
        b = hex_copy[i+1]

        if a in digits: hex_copy[i] = int(a)
        if b in digits: hex_copy[i+1] = int(b)

        byte = _two_hex_to_byte(hex_copy[i], hex_copy[i+1])
        byte_arr.append(byte)

    return byte_arr

def hex_to_bytes(hex_str):
    lst = hex_to_byte_lst(hex_str)
    return bytes_to_str(lst)


if __name__ == "__main__":
    # print(_two_hex_to_byte(7, 'f') == 127)
    # print(_two_hex_to_byte('a', 'a') == 170)

    # print(hex_to_byte("deadbeef123456"))

    print(hex_to_bytes("63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"))
    # crypto{You_will_be_working_with_hex_strings_a_lot}








