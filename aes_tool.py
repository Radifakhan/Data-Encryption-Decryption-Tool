import os
import base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def generate_key():
    """Generate a secure 256-bit AES key."""
    return AESGCM.generate_key(bit_length=256)


def encrypt_message(message, key):
    """Encrypt a message using AES-256-GCM."""
    aes = AESGCM(key)

    # Generate a unique 96-bit nonce
    nonce = os.urandom(12)

    # Encrypt the message
    ciphertext = aes.encrypt(
        nonce,
        message.encode("utf-8"),
        None
    )

    # Store nonce + ciphertext together
    encrypted_data = nonce + ciphertext

    return base64.b64encode(encrypted_data).decode("utf-8")


def decrypt_message(encrypted_data, key):
    """Decrypt an AES-256-GCM encrypted message."""
    try:
        aes = AESGCM(key)

        # Decode Base64
        data = base64.b64decode(encrypted_data)

        # Extract nonce and ciphertext
        nonce = data[:12]
        ciphertext = data[12:]

        # Decrypt
        plaintext = aes.decrypt(
            nonce,
            ciphertext,
            None
        )

        return plaintext.decode("utf-8")

    except Exception:
        return "Decryption failed: invalid key or modified data."


def main():
    print("=" * 50)
    print("       AES-256-GCM ENCRYPTION TOOL")
    print("=" * 50)

    key = generate_key()

    print("\nGenerated AES-256 key:")
    print(base64.b64encode(key).decode("utf-8"))

    message = input("\nEnter a message to encrypt: ")

    encrypted = encrypt_message(message, key)

    print("\nEncrypted message:")
    print(encrypted)

    decrypted = decrypt_message(encrypted, key)

    print("\nDecrypted message:")
    print(decrypted)

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()

