import string
import random

def generate_vigenere_table(alphabet):
  """Generates a Vigenère table using the given alphabet."""
  table = []
  for i in range(len(alphabet)):
    shifted_alphabet = alphabet[i:] + alphabet[:i]
    table.append(shifted_alphabet)
  return table

def generate_key(length, alphabet):
  """Generates a random key of the specified length from the given alphabet."""
  return ''.join(random.choices(alphabet, k=length))

def vigenere_encrypt(plaintext, key):
  """Encrypts the plaintext using the Vigenère cipher with the given key and table."""
  vigenere_table = generate_vigenere_table(string.ascii_uppercase)
  ciphertext = ""
  alphabet = string.ascii_uppercase
  key_index = 0
  for char in plaintext:
    if char.isalpha():
      row = alphabet.index(char.upper())
      col = alphabet.index(key[key_index % len(key)])
      new_char = vigenere_table[row][col]
      ciphertext += new_char
      key_index += 1
    else:
      ciphertext += char
  return ciphertext

def vigenere_decrypt(ciphertext, key):
  """Decrypts the ciphertext using the Vigenère cipher with the given key and table."""
  vigenere_table = generate_vigenere_table(string.ascii_uppercase)
  plaintext = ""
  alphabet = string.ascii_uppercase
  key_index = 0
  for char in ciphertext:
    if char.isalpha():
      row = alphabet.index(char.upper())
      col = key[key_index % len(key)]
      new_char = alphabet[vigenere_table[row].index(col)]
      plaintext += new_char
      key_index += 1
    else:
      plaintext += char
  return plaintext

def print_vigenere_table(alphabet):
  """Prints the Vigenère table in a user-friendly format."""
  table = generate_vigenere_table(alphabet)
  print("Vigenère Table:")
  print("  ", end="")
  for char in alphabet:
    print(char, end=" ")
  print()
  for i in range(len(alphabet)):
    print(alphabet[i], end=" ")
    for char in table[i]:
      print(char, end=" ")
    print()

def main():
  # Loop for sending three messages
  for _ in range(3):
    # Get plaintext input from user
    plaintext = input("Enter your message: ").upper()

    # Generate random key
    key_length = len(plaintext.replace(" ", ""))  # Adjust key length based on message (excluding spaces)
    key = generate_key(key_length, string.ascii_uppercase)
    print("Generated Key:", key)

    # Print Vigenère Table
    print_vigenere_table(string.ascii_uppercase)

    # Encrypt the message
    ciphertext = vigenere_encrypt(plaintext, key)
    print("Encrypted Message:", ciphertext)

    # Decrypt the message (simulating receiver)
    decrypted_message = vigenere_decrypt(ciphertext, key)
    print("Decrypted Message:", decrypted_message.lower())
    print()

if __name__ == "__main__":
  main()
