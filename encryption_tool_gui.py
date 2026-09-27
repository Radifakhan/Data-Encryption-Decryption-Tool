import os
import base64
import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


# ============================================================
# COLORS
# ============================================================

BG = "#08111F"
PANEL = "#0D1B2A"
CARD = "#10243A"
INPUT = "#071522"
ACCENT = "#00D9FF"
ACCENT2 = "#00FF9C"
TEXT = "#F1F5F9"
MUTED = "#94A3B8"
DANGER = "#FF5C7A"
WHITE = "#FFFFFF"


# ============================================================
# CRYPTOGRAPHIC FUNCTIONS
# ============================================================

def generate_aes_key():
    return AESGCM.generate_key(bit_length=256)


def aes_encrypt(message, key):
    aes = AESGCM(key)
    nonce = os.urandom(12)

    ciphertext = aes.encrypt(
        nonce,
        message.encode("utf-8"),
        None
    )

    return base64.b64encode(
        nonce + ciphertext
    ).decode("utf-8")


def aes_decrypt(encrypted_message, key):
    try:
        data = base64.b64decode(
            encrypted_message
        )

        nonce = data[:12]
        ciphertext = data[12:]

        aes = AESGCM(key)

        plaintext = aes.decrypt(
            nonce,
            ciphertext,
            None
        )

        return plaintext.decode("utf-8")

    except Exception:
        return None


def generate_rsa_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    return private_key, private_key.public_key()


def rsa_encrypt(message, public_key):

    ciphertext = public_key.encrypt(
        message.encode("utf-8"),

        padding.OAEP(
            mgf=padding.MGF1(
                algorithm=hashes.SHA256()
            ),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return base64.b64encode(
        ciphertext
    ).decode("utf-8")


def rsa_decrypt(encrypted_message, private_key):

    try:

        ciphertext = base64.b64decode(
            encrypted_message
        )

        plaintext = private_key.decrypt(
            ciphertext,

            padding.OAEP(
                mgf=padding.MGF1(
                    algorithm=hashes.SHA256()
                ),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        return plaintext.decode("utf-8")

    except Exception:
        return None


# ============================================================
# MAIN WINDOW
# ============================================================

root = tk.Tk()

root.title(
    "CipherShield - Data Encryption & Decryption Tool"
)

root.geometry("1100x750")

root.configure(
    bg=BG
)

root.resizable(False, False)


# ============================================================
# KEYS
# ============================================================

aes_key = generate_aes_key()

rsa_private_key, rsa_public_key = generate_rsa_keys()


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def clear_text():

    message_box.delete(
        "1.0",
        tk.END
    )

    result_box.delete(
        "1.0",
        tk.END
    )

    status_label.config(
        text="● Ready",
        fg=ACCENT2
    )


def set_status(text, color=ACCENT2):

    status_label.config(
        text="● " + text,
        fg=color
    )


def show_result(title, data):

    result_box.delete(
        "1.0",
        tk.END
    )

    result_box.insert(
        tk.END,
        title + "\n\n"
    )

    result_box.insert(
        tk.END,
        data
    )


# ============================================================
# AES MESSAGE
# ============================================================

def aes_encrypt_message():

    message = message_box.get(
        "1.0",
        "end-1c"
    )

    if not message:

        messagebox.showwarning(
            "Input Required",
            "Please enter a message first."
        )

        return

    encrypted = aes_encrypt(
        message,
        aes_key
    )

    show_result(
        "AES-256-GCM • ENCRYPTED MESSAGE",
        encrypted
    )

    set_status(
        "AES encryption completed"
    )


def aes_decrypt_message():

    encrypted = message_box.get(
        "1.0",
        "end-1c"
    )

    if not encrypted:

        messagebox.showwarning(
            "Input Required",
            "Enter the encrypted message."
        )

        return

    decrypted = aes_decrypt(
        encrypted,
        aes_key
    )

    if decrypted is None:

        messagebox.showerror(
            "Decryption Failed",
            "Invalid encrypted message or key."
        )

        set_status(
            "AES decryption failed",
            DANGER
        )

        return

    show_result(
        "AES-256-GCM • DECRYPTED MESSAGE",
        decrypted
    )

    set_status(
        "AES decryption completed"
    )


# ============================================================
# RSA MESSAGE
# ============================================================

def rsa_encrypt_message():

    message = message_box.get(
        "1.0",
        "end-1c"
    )

    if not message:

        messagebox.showwarning(
            "Input Required",
            "Please enter a message first."
        )

        return

    try:

        encrypted = rsa_encrypt(
            message,
            rsa_public_key
        )

        show_result(
            "RSA-2048-OAEP • ENCRYPTED MESSAGE",
            encrypted
        )

        set_status(
            "RSA encryption completed"
        )

    except Exception as error:

        messagebox.showerror(
            "Encryption Error",
            str(error)
        )


def rsa_decrypt_message():

    encrypted = message_box.get(
        "1.0",
        "end-1c"
    )

    if not encrypted:

        messagebox.showwarning(
            "Input Required",
            "Enter the encrypted message."
        )

        return

    decrypted = rsa_decrypt(
        encrypted,
        rsa_private_key
    )

    if decrypted is None:

        messagebox.showerror(
            "Decryption Failed",
            "Invalid RSA encrypted message."
        )

        set_status(
            "RSA decryption failed",
            DANGER
        )

        return

    show_result(
        "RSA-2048-OAEP • DECRYPTED MESSAGE",
        decrypted
    )

    set_status(
        "RSA decryption completed"
    )


# ============================================================
# FILE ENCRYPTION
# ============================================================

def encrypt_file():

    file_path = filedialog.askopenfilename(
        title="Select file to encrypt"
    )

    if not file_path:
        return

    try:

        with open(
            file_path,
            "rb"
        ) as file:

            data = file.read()

        nonce = os.urandom(12)

        encrypted = AESGCM(
            aes_key
        ).encrypt(
            nonce,
            data,
            None
        )

        output_path = (
            file_path + ".enc"
        )

        with open(
            output_path,
            "wb"
        ) as file:

            file.write(
                nonce + encrypted
            )

        key = base64.b64encode(
            aes_key
        ).decode()

        show_result(
            "FILE ENCRYPTION • AES-256-GCM",
            f"Original File:\n{file_path}\n\n"
            f"Encrypted File:\n{output_path}\n\n"
            f"AES-256 KEY:\n{key}"
        )

        set_status(
            "File encrypted successfully"
        )

    except Exception as error:

        messagebox.showerror(
            "Encryption Error",
            str(error)
        )


def decrypt_file():

    file_path = filedialog.askopenfilename(
        title="Select encrypted .enc file"
    )

    if not file_path:
        return

    try:

        with open(
            file_path,
            "rb"
        ) as file:

            encrypted_data = file.read()

        nonce = encrypted_data[:12]

        ciphertext = encrypted_data[12:]

        decrypted = AESGCM(
            aes_key
        ).decrypt(
            nonce,
            ciphertext,
            None
        )

        output_path = os.path.join(
            os.path.dirname(file_path),
            "decrypted_" +
            os.path.basename(file_path).replace(
                ".enc",
                ""
            )
        )

        with open(
            output_path,
            "wb"
        ) as file:

            file.write(
                decrypted
            )

        show_result(
            "FILE DECRYPTION • AES-256-GCM",
            f"Encrypted File:\n{file_path}\n\n"
            f"Decrypted File:\n{output_path}"
        )

        set_status(
            "File decrypted successfully"
        )

    except Exception:

        messagebox.showerror(
            "Decryption Failed",
            "The file is invalid, modified, or encrypted with another key."
        )

        set_status(
            "File decryption failed",
            DANGER
        )


# ============================================================
# HEADER
# ============================================================

header = tk.Frame(
    root,
    bg=PANEL,
    height=95
)

header.pack(
    fill="x"
)

header.pack_propagate(False)


title_frame = tk.Frame(
    header,
    bg=PANEL
)

title_frame.pack(
    side="left",
    padx=35,
    pady=15
)


tk.Label(
    title_frame,
    text="◈  CIPHERSHIELD",
    font=("Arial", 22, "bold"),
    fg=ACCENT,
    bg=PANEL
).pack(
    anchor="w"
)


tk.Label(
    title_frame,
    text="Data Encryption & Decryption Platform",
    font=("Arial", 10),
    fg=MUTED,
    bg=PANEL
).pack(
    anchor="w"
)


status_label = tk.Label(
    header,
    text="● Ready",
    font=("Arial", 11, "bold"),
    fg=ACCENT2,
    bg=PANEL
)

status_label.pack(
    side="right",
    padx=35
)


# ============================================================
# SECURITY CARDS
# ============================================================

security_frame = tk.Frame(
    root,
    bg=BG
)

security_frame.pack(
    pady=20
)


def security_card(
    parent,
    title,
    description
):

    card = tk.Frame(
        parent,
        bg=CARD,
        width=300,
        height=75
    )

    card.pack(
        side="left",
        padx=8
    )

    card.pack_propagate(False)

    tk.Label(
        card,
        text=title,
        font=("Arial", 11, "bold"),
        fg=ACCENT,
        bg=CARD
    ).pack(
        anchor="w",
        padx=15,
        pady=(10, 2)
    )

    tk.Label(
        card,
        text=description,
        font=("Arial", 9),
        fg=MUTED,
        bg=CARD
    ).pack(
        anchor="w",
        padx=15
    )


security_card(
    security_frame,
    "AES-256-GCM",
    "Symmetric • Confidentiality + Integrity"
)

security_card(
    security_frame,
    "RSA-2048-OAEP",
    "Asymmetric • Public/Private Key"
)

security_card(
    security_frame,
    "SECURE RANDOMNESS",
    "Cryptographically secure nonces"
)


# ============================================================
# MESSAGE PANEL
# ============================================================

main_frame = tk.Frame(
    root,
    bg=BG
)

main_frame.pack(
    padx=35,
    fill="x"
)


# LEFT PANEL

left_panel = tk.Frame(
    main_frame,
    bg=PANEL,
    width=500,
    height=350
)

left_panel.pack(
    side="left",
    padx=(0, 10)
)

left_panel.pack_propagate(False)


tk.Label(
    left_panel,
    text="MESSAGE INPUT",
    font=("Arial", 12, "bold"),
    fg=WHITE,
    bg=PANEL
).pack(
    anchor="w",
    padx=20,
    pady=(18, 5)
)


tk.Label(
    left_panel,
    text="Enter plaintext or encrypted data",
    font=("Arial", 9),
    fg=MUTED,
    bg=PANEL
).pack(
    anchor="w",
    padx=20
)


message_box = tk.Text(
    left_panel,
    height=9,
    width=55,
    bg=INPUT,
    fg=TEXT,
    insertbackground=ACCENT,
    font=("Consolas", 10),
    relief="flat",
    padx=12,
    pady=10
)

message_box.pack(
    padx=20,
    pady=12
)


# BUTTON FRAME

button_area = tk.Frame(
    left_panel,
    bg=PANEL
)

button_area.pack()


def make_button(
    parent,
    text,
    command,
    color
):

    return tk.Button(
        parent,
        text=text,
        command=command,
        font=("Arial", 9, "bold"),
        bg=color,
        fg=BG,
        activebackground=WHITE,
        activeforeground=BG,
        relief="flat",
        padx=14,
        pady=8,
        cursor="hand2"
    )


make_button(
    button_area,
    "AES ENCRYPT",
    aes_encrypt_message,
    ACCENT
).grid(
    row=0,
    column=0,
    padx=4
)


make_button(
    button_area,
    "AES DECRYPT",
    aes_decrypt_message,
    ACCENT2
).grid(
    row=0,
    column=1,
    padx=4
)


make_button(
    button_area,
    "RSA ENCRYPT",
    rsa_encrypt_message,
    ACCENT
).grid(
    row=0,
    column=2,
    padx=4
)


make_button(
    button_area,
    "RSA DECRYPT",
    rsa_decrypt_message,
    ACCENT2
).grid(
    row=0,
    column=3,
    padx=4
)


# RIGHT PANEL

right_panel = tk.Frame(
    main_frame,
    bg=PANEL,
    width=500,
    height=350
)

right_panel.pack(
    side="right",
    padx=(10, 0)
)

right_panel.pack_propagate(False)


tk.Label(
    right_panel,
    text="OPERATION RESULT",
    font=("Arial", 12, "bold"),
    fg=WHITE,
    bg=PANEL
).pack(
    anchor="w",
    padx=20,
    pady=(18, 5)
)


tk.Label(
    right_panel,
    text="Encrypted/decrypted output appears here",
    font=("Arial", 9),
    fg=MUTED,
    bg=PANEL
).pack(
    anchor="w",
    padx=20
)


result_box = tk.Text(
    right_panel,
    height=14,
    width=55,
    bg=INPUT,
    fg=ACCENT2,
    font=("Consolas", 9),
    relief="flat",
    padx=12,
    pady=10
)

result_box.pack(
    padx=20,
    pady=12
)


# ============================================================
# FILE OPERATIONS
# ============================================================

file_panel = tk.Frame(
    root,
    bg=PANEL,
    height=85
)

file_panel.pack(
    padx=35,
    pady=18,
    fill="x"
)

file_panel.pack_propagate(False)


tk.Label(
    file_panel,
    text="FILE SECURITY",
    font=("Arial", 11, "bold"),
    fg=WHITE,
    bg=PANEL
).pack(
    side="left",
    padx=20
)


make_button(
    file_panel,
    "📁  ENCRYPT FILE",
    encrypt_file,
    ACCENT
).pack(
    side="left",
    padx=10
)


make_button(
    file_panel,
    "🔓  DECRYPT FILE",
    decrypt_file,
    ACCENT2
).pack(
    side="left",
    padx=10
)


make_button(
    file_panel,
    "CLEAR",
    clear_text,
    "#CBD5E1"
).pack(
    side="right",
    padx=20
)


# ============================================================
# FOOTER
# ============================================================

footer = tk.Label(
    root,
    text="CYBERSHIELD  •  AES-256-GCM  •  RSA-2048-OAEP  •  CYBER SECURITY PROJECT",
    font=("Arial", 8),
    fg=MUTED,
    bg=BG
)

footer.pack(
    pady=2
)


root.mainloop()
