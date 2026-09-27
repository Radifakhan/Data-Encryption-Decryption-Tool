import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def generate_key():
    """Generate a secure 256-bit AES key."""
    return AESGCM.generate_key(bit_length=256)


def encrypt_file(input_file, output_file, key):
    """Encrypt a file using AES-256-GCM."""
    aes = AESGCM(key)

    with open(input_file, "rb") as file:
        data = file.read()

    nonce = os.urandom(12)

    encrypted_data = aes.encrypt(nonce, data, None)

    with open(output_file, "wb") as file:
        file.write(nonce + encrypted_data)

    print(f"File encrypted successfully: {output_file}")


def decrypt_file(input_file, output_file, key):
    """Decrypt an AES-256-GCM encrypted file."""
    try:
        aes = AESGCM(key)

        with open(input_file, "rb") as file:
            encrypted_data = file.read()

        nonce = encrypted_data[:12]
        ciphertext = encrypted_data[12:]

        decrypted_data = aes.decrypt(nonce, ciphertext, None)

        with open(output_file, "wb") as file:
            file.write(decrypted_data)

        print(f"File decrypted successfully: {output_file}")

    except Exception:
        print("Decryption failed: invalid key or modified file.")


def main():
    print("=" * 55)
    print("        AES-256-GCM FILE ENCRYPTION TOOL")
    print("=" * 55)

    key = generate_key()

    print("\nAES-256 key generated successfully.")

    input_file = input("\nEnter file to encrypt: ")

    if not os.path.exists(input_file):
        print("File not found.")
        return

    encrypted_file = input_file + ".enc"
    decrypted_file = "decrypted_" + input_file

    encrypt_file(input_file, encrypted_file, key)

    decrypt_file(encrypted_file, decrypted_file, key)

    print("\nFile encryption and decryption completed.")
    print("=" * 55)


if __name__ == "__main__":
    main()
