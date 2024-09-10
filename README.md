
# Ransomware Simulation

This project demonstrates a basic ransomware simulation with encryption and decryption capabilities. The ransomware encrypts files using AES encryption and hides the AES key using RSA encryption. A ransom note is created with a hint to find the real AES key among several fake keys.

---
### Encryption
![Encryption Process](https://d8it4huxumps7.cloudfront.net/uploads/images/650a96f7bf772_encryption_vs_decryption_02.jpg)
*(The image is taken from unstop )*
### Decryption
![Decryption Process](https://d8it4huxumps7.cloudfront.net/uploads/images/650a96d2732f2_encryption_vs_decryption_03.jpg?d=2000x2000) 
*(The image is taken from unstop )*

---

## Project Structure

- **`encryption.py`**: Encrypts files, generates RSA key pairs, and creates a ransom note.
- **`decryption.py`**: Decrypts files using a private key and an AES key obtained from the ransom note.
- **`key_finder.py`**: Finds the real private key by testing a set of fake keys.

---

## Requirements

- Python 3.7 or higher
- `cryptography` library

To install the required dependencies, run the following command:

```bash
pip install cryptography
```

---

## Usage

### Encryption

To generate RSA key pair and encrypt files, run `encryption.py`:

```bash
python encryption.py
```

This script will:

- Encrypt files in the `dummy_files/` directory.
- Create a ransom note with a hint.
- Generate a directory `good_luck_finding_the_key/` containing the AES key along with fake keys.
- Save the private RSA key in `private_key.pem`.

---

### Decryption

To find the real private key and decrypt files:

1. Run `key_finder.py` to identify the correct private key:
   
   ```bash
   python key_finder.py
   ```
you have to input the encrypted AES key value from the `ransom_note.txt` the it will tell which is the real key.

2. Run `decryption.py` with the correct private key to decrypt the files:

   ```bash
   python decryption.py
   ```
you have to input the location/directory of that real key which `key_finder.py` have given.

   The decryption script will:
   
   - Decrypt the files in `dummy_files/`.
   - Delete the `good_luck_finding_the_key/` folder and `ransom_note.txt`.

---

## Detailed Description

### Encryption Process

The `encryption.py` script performs the following tasks:

1. **Generate RSA Key Pair**: Creates public and private RSA keys.
2. **Generate AES Key**: Used for file encryption.
3. **Encrypt Files**: Encrypts files in the `dummy_files/` directory using the AES key.
4. **Encrypt AES Key**: The AES key is encrypted using the RSA public key.
5. **Create Ransom Note**: A ransom note is generated with the encrypted AES key and placed in the root directory.
6. **Save Private Key**: The RSA private key is saved in `private_key.pem`.

---

### Decryption Process

The `decryption.py` script decrypts the files using the following steps:

1. **Load Private Key**: Loads the RSA private key.
2. **Decrypt AES Key**: Decrypts the AES key using the private key.
3. **Decrypt Files**: Decrypts files in the `dummy_files/` directory using the decrypted AES key.
4. **Clean Up**: Removes the ransom note and the fake key folder.

---

### Key Finder

The `key_finder.py` script helps in finding the real private key among several fake keys by testing each key to find the correct one that can decrypt the AES key in the ransom note.

---

## Notes

- The `dummy_files/` directory should contain the files to be encrypted.
- Be careful when running the simulation on important files.
- Modify file paths and directories as necessary for your environment.

---

## License

This project in not been licensed under any License. You can are free to use and give your inputs.

  
---

Feel free to contribute, suggest new features, or report issues. Happy Encrypting! 😊

---

Remember: This project is for educational purposes only. Do not use this knowledge for illegal activities or unauthorized access to systems. Always adhere to ethical guidelines in cybersecurity practices.
