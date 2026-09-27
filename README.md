# CipherShield – Data Encryption & Decryption Tool

**Name:** Radifa Khanam    
**Project:** Data Encryption and Decryption Tool  
**Environment:** Kali Linux  
**Language:** Python 3.14.7  

---

## 1. Project Overview

CipherShield is a Python-based data encryption and decryption application developed as part of the Cyber Security and Ethical Hacking.

The project demonstrates practical implementation of symmetric and asymmetric cryptography using:

- AES-256-GCM
- RSA-2048-OAEP

The application supports secure message encryption/decryption and file encryption/decryption through a graphical user interface.

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

- 2048-bit asymmetric key pair
- Public-key encryption
- Private-key decryption
- OAEP padding
- SHA-256 hashing

### Graphical User Interface

- Cybersecurity-themed interface
- AES message encryption/decryption
- RSA message encryption/decryption
- File encryption
- File decryption
- Operation status indicator
- Result display

### Security Testing

- Successful encryption/decryption testing
- File encryption/decryption testing
- AES-GCM tamper detection testing
- AES vs RSA performance benchmarking

---

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.14.7 | Application development |
| Cryptography 50.0.1 | Cryptographic operations |
| Tkinter | Graphical user interface |
| AES-256-GCM | Symmetric encryption |
| RSA-2048-OAEP | Asymmetric encryption |
| SHA-256 | Cryptographic hashing |
| Kali Linux | Development and testing environment |

---

## 5. AES-256-GCM

AES is a symmetric encryption algorithm where the same secret key is used for encryption and decryption.

This project uses AES-256-GCM.

GCM provides authenticated encryption, which means that it provides:

- Confidentiality
- Integrity
- Authentication

A unique 12-byte nonce is generated for each encryption operation.

---

## 6. RSA-2048-OAEP

RSA is an asymmetric cryptographic algorithm.

It uses two keys:

- Public key – used for encryption
- Private key – used for decryption

The project uses RSA-2048 with OAEP padding and SHA-256.

RSA is useful for demonstrating public-key cryptography, while AES is more suitable for efficient encryption of larger amounts of data.

---

## 7. File Encryption

The application supports AES-256-GCM file encryption.

Encryption flow:

```text
Input File
    ↓
Read Binary Data
    ↓
Generate Secure Nonce
    ↓
AES-256-GCM Encryption
    ↓
Nonce + Encrypted Data
    ↓
Encrypted .enc File
