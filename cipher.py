def caesar_cipher_encrypt(text, shift = 5):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Convert character to lowercase
            char = char.lower()
            # Encrypt the character
            encrypted_char = chr((ord(char) + shift - 97) % 26 + 97)
            encrypted_text += encrypted_char
        else:
            # Preserve non-alphabetic characters
            encrypted_text += char
    return encrypted_text

plaintext = input("Please enter a senctence: ")

encrypted_text = caesar_cipher_encrypt(plaintext)
print("The encrypted sentence is:", encrypted_text)


