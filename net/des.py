from Crypto.Cipher import DES 
from Crypto.Util.Padding import pad, unpad 
from Crypto.Random import get_random_bytes 

def encrypt(plaintext, key): 
    cipher = DES.new(key, DES.MODE_ECB) 
    ciphertext = cipher.encrypt(pad(plaintext, DES.block_size)) 
    return ciphertext 

def decrypt(ciphertext, key): 
    cipher = DES.new(key, DES.MODE_ECB) 
    plaintext = unpad(cipher.decrypt(ciphertext), DES.block_size) 
    return plaintext 

key = get_random_bytes(8)  
plaintext = b"Hello, DES!" 
encrypted_data = encrypt(plaintext, key) 
decrypted_data = decrypt(encrypted_data, key) 

print("Plaintext:", plaintext) 
print("Encrypted data:", encrypted_data) 
print("Decrypted data:", decrypted_data)
