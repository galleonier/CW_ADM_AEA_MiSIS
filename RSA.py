import random
from sympy import isprime, mod_inverse
def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if isprime(num):
            return num
def generate_keys(bits):
    p = generate_prime(bits // 2)
    q = generate_prime(bits // 2)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    d = mod_inverse(e, phi)
    return (e, n), (d, n)
def encrypt(message, public_key):
    e, n = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message
def decrypt(encrypted_message, private_key):
    d, n = private_key
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in encrypted_message])
    return decrypted_message

public_key, private_key = generate_keys(32)
print(f"Открытый ключ: {public_key}")
print(f"Закрытый ключ: {private_key}")
message = "Hello"
print(f"Исходное сообщение: {message}")
encrypted_message = encrypt(message, public_key)
print(f"Зашифрованное сообщение: {encrypted_message}")
decrypted_message = decrypt(encrypted_message, private_key)
print(f"Расшифрованное сообщение: {decrypted_message}")
