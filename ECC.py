from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
private_key = ec.generate_private_key(ec.SECP256R1())
public_key = private_key.public_key()
message = b"Hello, ECC!"
signature = private_key.sign(message, ec.ECDSA(hashes.SHA256()))
try:
    public_key.verify(signature, message, ec.ECDSA(hashes.SHA256()))
    print("Подпись подтверждена")
except:
    print("Подпись не подтверждена")
private_bytes = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)
public_bytes = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
print(f"Закрытый ключ: {private_bytes.decode('utf-8')}")
print(f"Открытый ключ: {public_bytes.decode('utf-8')}")
loaded_private_key = serialization.load_pem_private_key(
    private_bytes,
    password=None
)
loaded_public_key = serialization.load_pem_public_key(
    public_bytes
)
loaded_public_key.verify(signature, message, ec.ECDSA(hashes.SHA256()))
print("Подпись проверена с использованием загруженного ключа")
