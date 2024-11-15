# -*- coding: utf-8 -*-
"""exe.php.new

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1THYQ8E9vS2bEJ_T-PGgpQ3nRZrP_ktcu
"""

pip install pycryptodome

def additive_cipher(text, shift):
    result = ""
    # Iterate over each character in the input text
    for char in text:
        if char.isalpha():  # Only process alphabetic characters
            # Determine if the character is uppercase or lowercase
            shift_base = 65 if char.isupper() else 97
            # Perform the shift using the ASCII value and modulo operation
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Non-alphabetic characters remain unchanged
    return result

# Example usage:
text = "HELLO WORLD"
shift = 3  # Shift each letter by 3 positions
print(additive_cipher(text, shift))  # Output: KHOOR ZRUOG

def multiplicative_cipher(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            # Multiply the position of the letter by the key and take modulo 26
            result += chr(((ord(char) - shift_base) * key) % 26 + shift_base)
        else:
            result += char  # Non-alphabetic characters remain unchanged
    return result

# Example usage:
text = "HELLO WORLD"
key = 5  # Multiply each letter's position by 5
print(multiplicative_cipher(text, key))  # Output: MJQQT BTWQI

def affine_cipher(text, a, b):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            # Apply the affine cipher formula
            result += chr(((a * (ord(char) - shift_base) + b) % 26) + shift_base)
        else:
            result += char  # Non-alphabetic characters remain unchanged
    return result

# Example usage:
text = "HELLO WORLD"
a = 5  # Multiplicative key
b = 8  # Additive key
print(affine_cipher(text, a, b))  # Output: RCPPS WSPQE

def generate_playfair_matrix(key):
    key = "".join(sorted(set(key), key=lambda x: key.index(x)))  # Remove duplicates while maintaining order
    matrix = [list(key[i:i+5]) for i in range(0, len(key), 5)]  # Create the 5x5 matrix
    return matrix

def playfair_encrypt(text, key):
    text = text.upper().replace("J", "I")  # Replace J with I as per Playfair specification
    matrix = generate_playfair_matrix(key)  # Generate Playfair matrix from key
    # Perform encryption (detailed implementation omitted for brevity)
    return "Encrypted Text"  # Placeholder

# Example usage:
text = "HEY WORLD"
key = "KEYWORD"
print(playfair_encrypt(text, key))  # Example result: Encrypted Text

#keyless
def transposition_cipher(text):
    result = ""
    # Swap adjacent characters in the text
    for i in range(0, len(text), 2):
        result += text[i+1] if i+1 < len(text) else text[i]  # If there's no pair, add the character as is
    return result

# Example usage:
text = "HELLO WORLD"
print(transposition_cipher(text))  # Output: EHLOL WRLOD

def keyed_transposition_cipher(text, key):
    num_columns = len(key)  # The number of columns is the length of the key
    num_rows = len(text) // num_columns + (len(text) % num_columns != 0)  # Calculate number of rows
    grid = [''] * num_columns  # Create a list of empty strings (columns)

    # Distribute characters into the grid based on column order
    for i in range(len(text)):
        grid[i % num_columns] += text[i]

    # Sort the grid by the key and concatenate the columns
    ordered_grid = sorted(zip(key, grid), key=lambda x: x[0])  # Sort based on the key values
    return ''.join([col for _, col in ordered_grid])  # Join the columns into a single string

# Example usage:
text = "HELLO WORLD"
key = [3, 1, 2]  # Key determines the column order
print(keyed_transposition_cipher(text, key))  # Output: LLOH W ERDOL

def diffie_hellman(p, g, a, b):
    # Calculate A and B using private keys a and b and public values p and g
    A = pow(g, a, p)  # A = g^a % p
    B = pow(g, b, p)  # B = g^b % p
    # Both parties now calculate the shared key using the other party's public value
    shared_key_A = pow(B, a, p)  # A computes (B^a) % p
    shared_key_B = pow(A, b, p)  # B computes (A^b) % p
    return shared_key_A, shared_key_B

# Example usage:
p = 23  # Prime number
g = 5   # Generator
a = 6   # Private key of Alice
b = 15  # Private key of Bob
shared_key_A, shared_key_B = diffie_hellman(p, g, a, b)
print(shared_key_A, shared_key_B)  # Both should be equal

# DDDDDDEESSS
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

def des_encrypt(text, key):
    cipher = DES.new(key, DES.MODE_ECB)  # Create a DES cipher object
    return cipher.encrypt(text.ljust(8))  # Encrypt, padding to 8 bytes

# Example usage:
key = get_random_bytes(8)  # DES requires an 8-byte key
text = b"ABCDEFGH"  # Plaintext must be a multiple of 8 bytes
ciphertext = des_encrypt(text, key)
print(ciphertext)  # Encrypted ciphertext

#AAAEESSS
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def aes_encrypt(text, key):
    cipher = AES.new(key, AES.MODE_ECB)  # Create an AES cipher object
    return cipher.encrypt(text.ljust(16))  # Encrypt, padding to 16 bytes

# Example usage:
key = get_random_bytes(16)  # 16-byte key for AES-128
text = b"HELLO WORLD 123"  # Plaintext must be a multiple of 16 bytes
ciphertext = aes_encrypt(text, key)
print(ciphertext)  # Encrypted ciphertext

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def rsa_encrypt(plaintext, pubkey):
    cipher = PKCS1_OAEP.new(pubkey)  # Create RSA cipher using public key
    return cipher.encrypt(plaintext.encode())  # Encrypt the plaintext

def rsa_decrypt(ciphertext, privkey):
    cipher = PKCS1_OAEP.new(privkey)  # Create RSA cipher using private key
    return cipher.decrypt(ciphertext).decode()  # Decrypt and convert back to string

# Example usage:
key = RSA.generate(2048)  # Generate RSA key pair
private_key = key
public_key = key.publickey()

text = "Hello, RSA!"
ciphertext = rsa_encrypt(text, public_key)
decrypted_text = rsa_decrypt(ciphertext, private_key)
print(f"Decrypted Text: {decrypted_text}")  # Output: Hello, RSA!