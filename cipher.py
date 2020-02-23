import random

""" for i in range(3):
    print ("I love Python")
print (range(26)) """

Letters = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(26)))

# print (tuple(Letters))

numbers = dict(zip(range(26), "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

# print (numbers)

for a in range(1):
    key = random.randint(1, 25)
    plaintext = input()
    ciphertext = ""

    for c in plaintext.upper():
        if c.isalpha():
            ciphertext += numbers[(Letters[c] + key)%26]
        else: ciphertext += c

    print (ciphertext)

    decrypt = ""

    for c in ciphertext:
        if c.isalpha():
            decrypt += numbers[(Letters[c] - key)%26]
        else:
            decrypt += c

    print (decrypt)

