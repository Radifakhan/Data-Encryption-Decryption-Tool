import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


key = AESGCM.generate_key(bit_length=256)
aes = AESGCM(key)

message = b"Confidential project data."

nonce = os.urandom(12)

encrypted = aes.encrypt(nonce, message, None)

print("Original message:")
print(message.decode())

# Modify one byte of the encrypted data
tampered = bytearray(encrypted)
tampered[0] ^= 1

try:
    aes.decrypt(nonce, bytes(tampered), None)
    print("\nTampered data was accepted.")
except Exception:
    print("\nTamper detected successfully!")
    print("AES-GCM rejected the modified encrypted data.")

