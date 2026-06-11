import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#ENCRYPT
plain_text = input("Enter a message to encrypt:")
ciper_text = ""

for letter in plain_text:
    index = chars.index(letter)
    ciper_text += key[index]
print(f"Original message: {plain_text}")
print(f"Encrypted message: {ciper_text}")

#DECRYPT
ciper_text = input("Enter a message to encrypt:")
plain_text = ""

for letter in ciper_text:
    index = key.index(letter)
    plain_text += chars[index]
print(f"Encrypted message: {ciper_text}")
print(f"Original message: {plain_text}")