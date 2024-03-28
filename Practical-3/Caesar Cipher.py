def encrypt(plain_text, key):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            ascii_offset = ord('a')
            encrypted_char = chr((ord(char.lower()) - ascii_offset + key) % 26 + ascii_offset)
            cipher_text += encrypted_char
        else:
            cipher_text += char
    return cipher_text

plain_text = input("Enter the plain text: ").lower()
key = int(input("Enter the key: "))

cipher_text = encrypt(plain_text, key)
print("Cipher text:", cipher_text)


# def mono_alphabetic_cipher(text, key):
#     encrypted_text = ""
#     for char in text:
#         if char.isalpha():
#             if char.isupper():
#                 encrypted_text += chr((ord(char) - 65 + key) % 26 + 65)
#             else:
#                 encrypted_text += chr((ord(char) - 97 + key) % 26 + 97)
#         else:
#             encrypted_text += char
#     return encrypted_text

# text = input("Enter the text to encrypt: ")
# key = int(input("Enter the key: "))

# encrypted_text = mono_alphabetic_cipher(text, key)
# print("Encrypted text:", encrypted_text)