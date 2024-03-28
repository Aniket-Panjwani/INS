import string
import random

def generate_key(length, alphabet):
  """Generates a random key of the specified length from the given alphabet."""
  return ''.join(random.choices(alphabet, k=length))

def vigenere_encrypt(plaintext, key):
  """Encrypts the plaintext using the Vigenère cipher with the given key."""
  ciphertext = ""
  alphabet = string.ascii_uppercase
  key_index = 0
  for char in plaintext:
    if char.isalpha():
      offset = alphabet.index(key[key_index % len(key)])
      new_char = chr((ord(char.upper()) + offset - ord('A')) % 26 + ord('A'))
      ciphertext += new_char
      key_index += 1
    else:
      ciphertext += char
  return ciphertext

def vigenere_decrypt(ciphertext, key):
  """Decrypts the ciphertext using the Vigenère cipher with the given key."""
  plaintext = ""
  alphabet = string.ascii_uppercase
  key_index = 0
  for char in ciphertext:
    if char.isalpha():
      offset = alphabet.index(key[key_index % len(key)])
      new_char = chr((ord(char.upper()) - offset - ord('A')) % 26 + ord('A'))
      plaintext += new_char
      key_index += 1
    else:
      plaintext += char
  return plaintext

def main():
  # Loop for sending three messages
  for _ in range(3):
    # Get plaintext input from user
    plaintext = input("Enter your message: ").upper()

    # Generate random key
    key_length = len(plaintext.replace(" ", ""))  # Adjust key length based on message (excluding spaces)
    key = generate_key(key_length, string.ascii_uppercase)
    print("Generated Key:", key)

    # Encrypt the message
    ciphertext = vigenere_encrypt(plaintext, key)
    print("Encrypted Message:", ciphertext)

    # Decrypt the message (simulating receiver)
    decrypted_message = vigenere_decrypt(ciphertext, key)
    print("Decrypted Message:", decrypted_message.lower())
    print()

if __name__ == "__main__":
  main()
