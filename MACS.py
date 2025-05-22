import random

def rotate_left_4(num: int, shift: int) -> int:
    shift %= 4
    return ((num << shift) | (num >> (4 - shift))) & 0xF

def rotate_right_4(num: int, shift: int) -> int:
    shift %= 4
    return ((num >> shift) | (num << (4 - shift))) & 0xF

def is_prime(n: int) -> bool:
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def generate_prime() -> int:
    primes = [p for p in range(2, 251) if is_prime(p)]
    return random.choice(primes)

def encrypt(plaintext: str) -> list[int]:
    p = generate_prime()
    upper_p = (p >> 4) & 0xF  # Extract upper 4 bits of p
    lower_p = p & 0xF          # Extract lower 4 bits of p
    r_upper = (upper_p % 3) + 1
    r_lower = (lower_p % 3) + 1
    ciphertext = [p]
    for char in plaintext:
        n = ord(char)
        upper = (n >> 4) & 0xF   # Split upper 4 bits
        lower = n & 0xF          # Split lower 4 bits
        # Rotate each half
        upper_rot = rotate_left_4(upper, r_upper)
        lower_rot = rotate_left_4(lower, r_lower)
        combined = (upper_rot << 4) | lower_rot
        encrypted = combined ^ p  # XOR with p
        ciphertext.append(encrypted)
    return ciphertext

def decrypt(ciphertext: list[int]) -> str:
    p = ciphertext[0]
    upper_p = (p >> 4) & 0xF
    lower_p = p & 0xF
    r_upper = (upper_p % 3) + 1
    r_lower = (lower_p % 3) + 1
    plaintext = []
    for c in ciphertext[1:]:
        combined = c ^ p  # Reverse XOR
        upper_rot = (combined >> 4) & 0xF
        lower_rot = combined & 0xF
        # Reverse rotations
        upper = rotate_right_4(upper_rot, r_upper)
        lower = rotate_right_4(lower_rot, r_lower)
        decrypted = (upper << 4) | lower
        plaintext.append(chr(decrypted))
    return ''.join(plaintext)

# Test Case
plaintext = "Sultan Mahamud Opu"
encrypted = encrypt(plaintext)
decrypted = decrypt(encrypted)

print(f"Plaintext: {plaintext}")
print(f"Ciphertext (with embedded key): {encrypted}")
print(f"Decrypted: {decrypted}")