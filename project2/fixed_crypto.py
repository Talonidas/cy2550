!/bin/env python3

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

def encrypt_file(input_file_path: str, output_file_path: str) -> bytes:
    """
    Encrypts a file using AES-256-GCM.
    
    Returns:
        bytes: The randomly generated 256-bit AES key. 
               Keep this secure to decrypt the file later.
    """
    # 1. Generate a secure 256-bit (32 bytes) key and a 96-bit (12 bytes) nonce
    key = AESGCM.generate_key(bit_length=256)
    nonce = os.urandom(12)
    
    aesgcm = AESGCM(key)
    
    # 2. Read plaintext data from the source file
    with open(input_file_path, 'rb') as f:
        plaintext = f.read()

    # 3. Encrypt data (AESGCM automatically appends an authentication tag)
    ciphertext = aesgcm.encrypt(nonce, plaintext, associated_data=None)
    
    # 4. Save the nonce and ciphertext to the target file
    # Prepending the nonce is safe and necessary for decryption
    with open(output_file_path, 'wb') as f:
        f.write(nonce + ciphertext)

    return key
#Placeholder
