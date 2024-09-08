import os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding as asymmetric_padding
from cryptography.hazmat.primitives import hashes

def try_key(fake_key_path, encrypted_aes_key):
    """Try a fake key to see if it can decrypt the AES key"""
    try:
        with open(fake_key_path, 'rb') as key_file:
            private_key = serialization.load_pem_private_key(key_file.read(), password=None)
        aes_key = private_key.decrypt(
            encrypted_aes_key,
            asymmetric_padding.OAEP(
                mgf=asymmetric_padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return aes_key
    except Exception:
        return None

def find_real_key(encrypted_aes_key, fake_key_dir):
    """Find the real AES key among fake keys"""
    for filename in os.listdir(fake_key_dir):
        fake_key_path = os.path.join(fake_key_dir, filename)
        if os.path.isfile(fake_key_path):
            print(f"Trying key in {fake_key_path}...")
            aes_key = try_key(fake_key_path, encrypted_aes_key)
            if aes_key:
                print(f"Real key found in file: {filename}")
                return aes_key
    raise ValueError("Real key not found among fake keys.")

def main():
    encrypted_aes_key_hex = input("Enter the encrypted AES key (from the ransom note) in hex: ")
    encrypted_aes_key = bytes.fromhex(encrypted_aes_key_hex)
    fake_key_dir = 'good_luck_finding_the_key'

    try:
        aes_key = find_real_key(encrypted_aes_key, fake_key_dir)
        print("Successfully found the real private key!")
        print(f"Real AES key: {aes_key.hex()}")
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()
