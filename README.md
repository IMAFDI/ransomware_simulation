
# Ransomware Simulation

This project demonstrates a basic ransomware simulation with encryption and decryption capabilities. The ransomware encrypts files using AES encryption and hides the AES key using RSA encryption. A ransom note is created with a hint to find the real AES key among several fake keys.

## Project Structure

- **`encryption.py`**: Encrypts files, generates RSA key pairs, and creates a ransom note.
- **`decryption.py`**: Decrypts files using a private key and an AES key obtained from the ransom note.
- **`key_finder.py`**: Finds the real private key by testing a set of fake keys.

## Requirements

- Python 3.7 or higher
- `cryptography` library

Install the required Python package using pip:

```bash
pip install cryptography
```
## Usage

## Encryption

Generate RSA Key Pair and Encrypt Files:

Run encryption.py to encrypt files in the dummy_files directory, create a ransom note, and save the private key for decryption.
```bash
python encryption.py
```
Important Files Created:

	•	ransom_note.txt: Contains a hint for finding the real AES key.
	•	good_luck_finding_the_key/: Directory containing fake keys and one real key.
	•	private_key.pem: Private RSA key used for decryption.

## Decryption

Find the Real Private Key:

Run key_finder.py to identify the real private key from the fake keys. You will need to provide the encrypted AES key from the ransom note.
```bash
python key_finder.py
```
Decrypt Files:

After finding the real private key, run decryption.py to decrypt the files. You will need to provide the path to the private key file.
```bash
python decryption.py
```
Actions Performed:

	•	Decrypts files in the dummy_files directory.
	•	Deletes the good_luck_finding_the_key/ folder and ransom_note.txt file after decryption.

Detailed Description

## Encryption

The encryption.py script performs the following tasks:

	1.	Generates RSA Key Pair: Creates a public and private key for encrypting and decrypting the AES key.
	2.	Generates AES Key: Creates a random AES key used for file encryption.
	3.	Encrypts Files: Encrypts files in the dummy_files directory using AES encryption with a randomly generated key.
	4.	Encrypts AES Key: Encrypts the AES key using the RSA public key.
	5.	Creates Ransom Note: Saves the encrypted AES key in a ransom note and places it in the root directory.
	6.	Saves Private Key: Saves the RSA private key in private_key.pem for later decryption.

## Decryption

The decryption.py script performs the following tasks:

	1.	Loads Private Key: Loads the RSA private key from a provided file.
	2.	Decrypts AES Key: Decrypts the AES key using the RSA private key.
	3.	Decrypts Files: Decrypts files in the dummy_files directory using the decrypted AES key.
	4.	Cleans Up: Deletes the good_luck_finding_the_key/ folder and ransom_note.txt file.

## Key Finder

The key_finder.py script helps in finding the real private key:

	•	Finds Real Private Key: Tests each fake key to find the real private key by attempting to decrypt the AES key from the ransom note.

Notes

	•	Ensure that the dummy_files directory contains the files you want to encrypt.
	•	Be cautious when running this simulation on important files, as it is designed to simulate ransomware behavior.
	•	Adjust file paths and directory names in the scripts as necessary for your environment.

License

This project is licensed under the MIT License. See the LICENSE file for details.

