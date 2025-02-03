# SarpTech Crypto Module
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def encrypt(message, key) -> str:
    salt = b"1234567890abcdef"  # Gerçek kullanımda sabit veya veritabanında saklanan bir salt kullan

    # PBKDF2 ile 32 baytlık bir anahtar türetme
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,  # Daha yüksek iterasyon daha güvenli ama daha yavaş
    )

    key = base64.urlsafe_b64encode(kdf.derive(key.encode()))

    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode()).decode()

    return encrypted_message

def decrypt(message, key) -> str:
    salt = b"1234567890abcdef"  # Gerçek kullanımda sabit veya veritabanında saklanan bir salt kullan

    # PBKDF2 ile 32 baytlık bir anahtar türetme
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,  # Daha yüksek iterasyon daha güvenli ama daha yavaş
    )

    key = base64.urlsafe_b64encode(kdf.derive(key.encode()))

    fernet = Fernet(key)
    decrypted_msg = fernet.decrypt(message).decode()
    return decrypted_msg

