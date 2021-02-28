import binascii
import properties

lemur = "lemur_ed66878c338e662d3473f0d98eedbd0d.png"
flag = "flag_7ae18c704272532658c10b5faad06d74.png"

if __name__ == "__main__":

    with open(lemur, 'rb') as f:
        s = f.read()

    with open(flag, 'rb') as g:
        t = g.read()

    len_first = 0
    while(s[len_first] == t[len_first]):
        len_first = len_first + 1

    png_bytes = s[:len_first]

    key = properties.xor_hex(s[len_first:].hex(), t[len_first:].hex())
    key = png_bytes + bytes.fromhex(key)

    print(key.hex())

    with open('key2.png', 'wb') as f:
        # for whatever reason, this does not seem to write all the bytes, the png comes out black after a certain point.
        # So I just used an online tool to XOR the images and got the flag crypto{x0Rly_n0t!} or something like that
        f.write(key)


