import random
from sympy import isprime
def generate_large_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if isprime(num):
            return num
def generate_keys(p, g):
    private_key = random.randint(2, p - 2)
    public_key = pow(g, private_key, p)
    return private_key, public_key
def compute_shared_secret(public_key, private_key, p):
    return pow(public_key, private_key, p)
p = generate_large_prime(128)
g = random.randint(2, p - 1)
alice_private_key, alice_public_key = generate_keys(p, g)
print(f"Алиса - Закрытый ключ: {alice_private_key}")
print(f"Алиса - Открытый ключ: {alice_public_key}")
bob_private_key, bob_public_key = generate_keys(p, g)
print(f"Боб - Закрытый ключ: {bob_private_key}")
print(f"Боб - Открытый ключ: {bob_public_key}")
alice_shared_secret = compute_shared_secret(bob_public_key, alice_private_key, p)
bob_shared_secret = compute_shared_secret(alice_public_key, bob_private_key, p)
print(f"Алиса - Общий секрет: {alice_shared_secret}")
print(f"Боб - Общий секрет: {bob_shared_secret}")
assert alice_shared_secret == bob_shared_secret, "Общий секрет не совпадает!"
print("Общий секрет успешно совпадает.")
