import binascii
import properties

lemur = "lemur_ed66878c338e662d3473f0d98eedbd0d.png"
flag = "flag_7ae18c704272532658c10b5faad06d74.png"

if __name__ == "__main__":

    with open(lemur, 'rb') as f:
        s = f.read()

    with open(flag, 'rb') as g:
        t = g.read()

    key = properties.xor_hex(s.hex(), t.hex())

    data = bytes.fromhex(key)
    print(data)

    with open('key.png', 'wb') as f:
        f.write(data)


