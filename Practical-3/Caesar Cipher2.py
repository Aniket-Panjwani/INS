def decrypt(cipher_text, key):
    plaintext = ""
    for char in cipher_text:
        if char.isalpha():
            ascii_val = ord(char)
            decrypted_val = (ascii_val - key) % 26
            decrypted_char = chr(decrypted_val + ord('A'))
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

def find_all_plaintexts(cipher_text):
    all_plaintexts = []
    for key in range(26):
        plaintext = decrypt(cipher_text, key)
        all_plaintexts.append(plaintext)
    return all_plaintexts

cipher_text = input("Enter the cipher text: ")
plaintexts = find_all_plaintexts(cipher_text)
print("All possible plaintexts:")
for plaintext in plaintexts:
    print(plaintext)