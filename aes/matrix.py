
def bytes2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
    plaintext_bytes = ""

    for row in matrix:
        # assuming each how has 4 bytes.. eg something like [19, 121, 225, 57]
        for i in range(0, 4):
            plaintext_bytes = plaintext_bytes + chr(row[i])

    return plaintext_bytes

def print2d(array):

    for row in array:
        n = len(row)
        row_output = ""

        for i in range(0, n-1):
            row_output = row_output + "{:3d}  ".format(row[i])

        row_output = row_output + "{:3d}".format(row[n-1])
        print(row_output)


if __name__ == "__main__":

    # this is the matrix which i have to decrypt..
    # the flag encrypts the plaintext crypto{inmatrix}
    matrix = [
        [99, 114, 121, 112],
        [116, 111, 123, 105],
        [110, 109, 97, 116],
        [114, 105, 120, 125],
    ]



    print(bytes2matrix("sixteencharacter"))

    # the string deadbeef in hex is repeated 4 times, making for 16 bytes
    # (two hex strings convert to one byte)
    deadbeef_bytes = bytes.fromhex("deadbeefdeadbeefdeadbeefdeadbeef")

    print(bytes2matrix(deadbeef_bytes))
    
    
    print(matrix2bytes(matrix))
