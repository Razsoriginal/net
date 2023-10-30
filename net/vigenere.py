def vigenere_encrypt(plain_text, key):
    key = key.upper()
    encrypted_text = ""
    key_len = len(key)
    
    for i, char in enumerate(plain_text):
        if char.isalpha():
            key_char = key[i % key_len]
            shift = ord(key_char) - ord('A')
            if char.isupper():
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            else:
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    return encrypted_text

# Example usage:
key = "KEY"
message = "HELLO WORLD"

encrypted_text = vigenere_encrypt(message, key)
print("Encrypted:", encrypted_text)
