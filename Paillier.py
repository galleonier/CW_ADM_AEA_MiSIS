import random
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def lcm(a, b):
    return abs(a * b) // gcd(a, b)
def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1
class Paillier:
    def __init__(self, bit_length=512):
        self.bit_length = bit_length
        self.public_key, self.private_key = self.generate_keys()
    def generate_prime(self, bit_length):
        while True:
            prime_candidate = random.getrandbits(bit_length)
            if self.is_prime(prime_candidate):
                return prime_candidate
    def is_prime(self, n, k=5):  # Miller-Rabin test
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0:
            return False
        r, s = 0, n - 1
        while s % 2 == 0:
            r += 1
            s //= 2
        for _ in range(k):
            a = random.randrange(2, n - 1)
            x = pow(a, s, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True
    def generate_keys(self):
        p = self.generate_prime(self.bit_length // 2)
        q = self.generate_prime(self.bit_length // 2)
        n = p * q
        g = n + 1
        lambda_ = lcm(p-1, q-1)
        mu = modinv(lambda_, n)
        public_key = (n, g)
        private_key = (lambda_, mu)
        return public_key, private_key
    def encrypt(self, m):
        n, g = self.public_key
        r = random.SystemRandom().randrange(1, n)
        c = (pow(g, m, n**2) * pow(r, n, n**2)) % (n**2)
        return c
    def decrypt(self, c):
        n, g = self.public_key
        lambda_, mu = self.private_key
        x = pow(c, lambda_, n**2) - 1
        l = (x // n) % n
        m = (l * mu) % n
        return m
paillier = Paillier(bit_length=32)
message = 12345
ciphertext = paillier.encrypt(message)
decrypted_message = paillier.decrypt(ciphertext)
print("Сообщение:", message)
print("Зашифрованное сообщение:", ciphertext)
print("Расшифрованное сообщение:", decrypted_message)
