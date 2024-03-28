def encrypt_mono_alpha(text, key):
    encrypted = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted += key[ord(char) - ord('a')]
            else:
                encrypted += key[ord(char) - ord('A')]
        else:
            encrypted += char
    return encrypted

key = "QWERTYUIOPASDFGHJKLZXCVBNM"
text = input("Enter text: ")

encrypted = encrypt_mono_alpha(text, key)

print("Encrypted text:", encrypted)