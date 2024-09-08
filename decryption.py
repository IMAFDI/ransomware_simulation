import os
import shutil
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding as asymmetric_padding

def load_private_key(private_key_path):
    """Load the private key from a file"""
    with open(private_key_path, 'rb') as private_key_file:
        private_key = serialization.load_pem_private_key(
            private_key_file.read(),
            password=None,
        )
    return private_key

def decrypt_aes_key(encrypted_aes_key, private_key):
    """Decrypt the AES key using RSA"""
    decrypted_aes_key = private_key.decrypt(
        encrypted_aes_key,
        asymmetric_padding.OAEP(
            mgf=asymmetric_padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_aes_key

def decrypt_file(file_path, aes_key):
    """Decrypt the encrypted file using the AES key"""
    with open(file_path, 'rb') as file:
        iv = file.read(16)  # First 16 bytes are the IV
        encrypted_data = file.read()

    cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv))
    decryptor = cipher.decryptor()

    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

    with open(file_path, 'wb') as decrypted_file:
        decrypted_file.write(unpadded_data)

def get_encrypted_aes_key_from_ransom_note():
    """Read the encrypted AES key from the ransom note"""
    with open('ransom_note.txt', 'r') as ransom_note_file:
        ransom_note = ransom_note_file.read()

    try:
        # Extract the encrypted AES key from the ransom note
        encrypted_aes_key_hex = ransom_note.split('decryption key hidden among the fake keys: ')[1].strip()
        return bytes.fromhex(encrypted_aes_key_hex)
    except IndexError:
        raise ValueError("Error reading encrypted AES key from ransom note: The ransom note does not contain the decryption key.")

def clean_up():
    """Delete the good_luck_finding_the_key folder and ransom_note.txt file"""
    if os.path.exists('good_luck_finding_the_key'):
        shutil.rmtree('good_luck_finding_the_key')
        print("Deleted the 'good_luck_finding_the_key' folder.")
    else:
        print("'good_luck_finding_the_key' folder not found.")
    
    if os.path.exists('ransom_note.txt'):
        os.remove('ransom_note.txt')
        print("Deleted the 'ransom_note.txt' file.")
    else:
        print("'ransom_note.txt' file not found.")

def main():
    private_key_path = input("Enter the path to the private key file: ")
    private_key = load_private_key(private_key_path)

    try:
        encrypted_aes_key = get_encrypted_aes_key_from_ransom_note()
        aes_key = decrypt_aes_key(encrypted_aes_key, private_key)

        for file in os.listdir('dummy_files'):
            file_path = os.path.join('dummy_files', file)
            decrypt_file(file_path, aes_key)

        print("All files have been decrypted.")
    except ValueError as e:
        print(e)
    finally:
        clean_up()

if __name__ == '__main__':
    main()
