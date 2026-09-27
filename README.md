# CipherShield – Data Encryption & Decryption Tool

**Project:** Data Encryption and Decryption Tool  
**Environment:** Kali Linux  
**Language:** Python 3.14.7  

---

## 1. Project Overview

CipherShield is a Python-based data encryption and decryption application designed to demonstrate practical implementation of modern cryptographic techniques.

The project demonstrates both symmetric and asymmetric cryptography using:

- AES-256-GCM
- RSA-2048-OAEP

The application supports secure message encryption/decryption and file encryption/decryption through a graphical user interface and command-line tools.

---

## 2. Objectives

The main objectives of this project are:

1. Implement AES encryption and decryption.
2. Implement RSA encryption and decryption.
3. Support secure file encryption and decryption.
4. Demonstrate confidentiality and integrity protection.
5. Demonstrate tamper detection using AES-GCM authentication.
6. Compare AES and RSA encryption performance.
7. Provide a simple cybersecurity-focused graphical interface.

---

## 3. Key Features

### AES-256-GCM

- 256-bit symmetric encryption
- Secure random nonce generation
- Authenticated encryption
- Tamper detection
- Message encryption/decryption
- File encryption/decryption

### RSA-2048-OAEP

- 2048-bit asymmetric encryption
- Public and private key generation
- OAEP padding
- Message encryption/decryption
- Secure asymmetric cryptography demonstration

### File Encryption

- Encrypt files using AES-based encryption
- Decrypt encrypted files
- Preserve decrypted file contents
- Verify successful encryption and decryption

### Graphical User Interface

- User-friendly Tkinter interface
- AES encryption/decryption
- RSA encryption/decryption
- File encryption/decryption
- Clear input and output sections

---

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.14.7 | Application development |
| Cryptography 50.0.1 | Cryptographic operations |
| AES-256-GCM | Symmetric encryption |
| RSA-2048-OAEP | Asymmetric encryption |
| Tkinter | Graphical user interface |
| Kali Linux | Development and testing environment |
| Git & GitHub | Version control and project hosting |

---

## 5. Testing

The project includes:

- AES encryption and decryption testing
- RSA encryption and decryption testing
- File encryption and decryption testing
- AES-GCM tamper detection testing
- AES vs RSA performance testing

Performance results are stored in:

`performance_results.txt`

---

## 6. Security

CipherShield demonstrates important cybersecurity concepts including:

- Data confidentiality
- Data integrity
- Authenticated encryption
- Tamper detection
- Symmetric cryptography
- Asymmetric cryptography
- Secure file handling

---

## 7. Project Structure

```text
Data-Encryption-Decryption-Tool/
│
├── aes_tool.py
├── rsa_tool.py
├── encryption_tool_gui.py
├── file_encryption.py
├── performance_test.py
├── tamper_test.py
├── performance_results.txt
├── test_message.txt
├── requirements.txt
├── README.md
│
├── screenshots/
│   ├── main-gui.png
│   ├── aes-encryption.png
│   ├── aes-decryption.png
│   ├── rsa-encryption.png
│   ├── rsa-decryption.png
│   ├── file-encryption.png
│   └── file-decryption.png
│
└── report/
    └── Data encryption and decryption tool.pdf
