def encrypt(plain_text, key):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            if char.isupper():
                index = ord(char) - ord('A')
                cipher_char = key[index].upper()
            else:
                index = ord(char) - ord('a')
                cipher_char = key[index].lower()
            cipher_text += cipher_char
        else:
            cipher_text += char
    return cipher_text

def decrypt(cipher_text, key):
    plain_text = ""
    for char in cipher_text:
        if char.isalpha():
            if char.isupper():
                index = ord(char) - ord('A')
                plain_char = chr(key[index].upper())
            else:
                index = ord(char) - ord('a')
                plain_char = chr(key[index].lower())
            plain_text += plain_char
        else:
            plain_text += char
    return plain_text

def main():
    key = []
    for i in range(26):
        key.append(input(f"Enter the key for '{chr(ord('a')+i)}': "))
    plain_text = input("Enter the plain text: ")
    cipher_text = encrypt(plain_text, key)
    print("Encrypted text:", cipher_text)
   

if __name__ == "__main__":
    main()