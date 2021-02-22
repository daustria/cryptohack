if __name__ == "__main__":
    s = "label"
    res = []

    for c in s:
        res.append(ord(c)^13)

    for i in range(0, len(res)):
        res[i] = chr(res[i])

    res = ''.join(res)

    # aloha
    print(res)


