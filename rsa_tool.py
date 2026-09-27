from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
import base64


def generate_keys():
    """Generate a 2048-bit RSA key pair."""
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    public_key = private_key.public_key()

    return private_key, public_key


def encrypt_message(message, public_key):
    """Encrypt a message using the RSA public key."""
    ciphertext = public_key.encrypt(
        message.encode("utf-8"),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return base64.b64encode(ciphertext).decode("utf-8")


def decrypt_message(encrypted_message, private_key):
    """Decrypt an RSA encrypted message using the private key."""
    try:
        ciphertext = base64.b64decode(encrypted_message)

        plaintext = private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        return plaintext.decode("utf-8")

    except Exception:
        return "Decryption failed."


def main():
    print("=" * 50)
    print("        RSA-2048 ENCRYPTION TOOL")
    print("=" * 50)

    private_key, public_key = generate_keys()

    print("\nRSA-2048 key pair generated successfully.")

    message = input("\nEnter a message to encrypt: ")

    encrypted = encrypt_message(message, public_key)

    print("\nEncrypted message:")
    print(encrypted)

    decrypted = decrypt_message(encrypted, private_key)

    print("\nDecrypted message:")
    print(decrypted)

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()

