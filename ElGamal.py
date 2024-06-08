import random
from sympy import isprime, mod_inverse
def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if isprime(num):
            return num
def generate_keys(bits):
    p = generate_prime(bits)
    g = random.randint(2, p - 1)
    x = random.randint(2, p - 2)
    y = pow(g, x, p)
    return (p, g, y), x
def encrypt(message, public_key):
    p, g, y = public_key
    m = int.from_bytes(message.encode(), 'big')
    k = random.randint(2, p - 2)
    a = pow(g, k, p)
    b = (m * pow(y, k, p)) % p
    return (a, b)
def decrypt(ciphertext, private_key, public_key):
    p, g, y = public_key
    a, b = ciphertext
    x = private_key
    s = pow(a, x, p)
    s_inv = mod_inverse(s, p)
    m = (b * s_inv) % p
    message = m.to_bytes((m.bit_length() + 7) // 8, 'big').decode()
    return message
public_key, private_key = generate_keys(128)
print(f"Открытый ключ: {public_key}")
print(f"Закрытый ключ: {private_key}")
message = "Hello, ElGamal!"
print(f"Исходное сообщение: {message}")
ciphertext = encrypt(message, public_key)
print(f"Зашифрованное сообщение: {ciphertext}")
decrypted_message = decrypt(ciphertext, private_key, public_key)
print(f"Расшифрованное сообщение: {decrypted_message}")
