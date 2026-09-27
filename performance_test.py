import time
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


# Test message
message = b"Glowlogics Cyber Security Internship Project - Encryption Performance Test."


# ============================================================
# AES-256-GCM
# ============================================================

aes_key = AESGCM.generate_key(bit_length=256)
aes = AESGCM(aes_key)

start = time.perf_counter()

for _ in range(1000):
    nonce = b"123456789012"
    aes.encrypt(nonce, message, None)

aes_time = time.perf_counter() - start


# ============================================================
# RSA-2048-OAEP
# ============================================================

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()

start = time.perf_counter()

for _ in range(100):
    public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(
                algorithm=hashes.SHA256()
            ),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

rsa_time = time.perf_counter() - start


# ============================================================
# RESULTS
# ============================================================

print("=" * 60)
print("        AES vs RSA PERFORMANCE COMPARISON")
print("=" * 60)

print("\nTest message size:", len(message), "bytes")

print("\nAES-256-GCM")
print("Iterations: 1000")
print("Total time: {:.6f} seconds".format(aes_time))
print("Average time: {:.6f} ms".format(
    (aes_time / 1000) * 1000
))

print("\nRSA-2048-OAEP")
print("Iterations: 100")
print("Total time: {:.6f} seconds".format(rsa_time))
print("Average time: {:.6f} ms".format(
    (rsa_time / 100) * 1000
))

print("\n" + "=" * 60)
