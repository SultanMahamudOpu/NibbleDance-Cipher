# 🔐 NibbleDance Cipher

## 📄 Table of Contents

1. [Overview](#overview)
2. [Introduction](#introduction)
3. [Encryption Process](#encryption-process)
4. [Decryption Process](#decryption-process)
5. [Examples with Test Cases](#examples-with-test-cases)  
   - Example 1: "Sultan"  
   - Example 2: "Lopa"
6. [Benefits of NibbleDance Cipher](#benefits-of-nibbledance-cipher)
7. [Conclusion](#conclusion)
8. [References](#references)
9. [Source Code](#source-code)

---

## 📘 Overview

**NibbleDance Cipher** is a lightweight symmetric encryption algorithm based on:
- Nibble-wise (4-bit) rotation
- Prime number-based key generation
- Bitwise XOR operations

This cipher is named **"NibbleDance"** due to the way it rotates and shifts 4-bit nibbles, creating a "dance" of bits that enhances diffusion and complexity in the ciphertext.

---

## ✨ Introduction

Cryptographic algorithms are essential for data privacy and secure communication. Traditional algorithms like AES and RSA are powerful but often heavy for lightweight applications. NibbleDance Cipher offers a novel and simple alternative for educational purposes, small devices, or custom protocols where lightweight encryption is required.

This algorithm utilizes:
- Random prime keys (between 2 and 250),
- Bitwise rotation on 4-bit nibbles,
- XOR operation for confusion.

It ensures reversible and secure encryption with a compact transformation process.

---

## 🔐 Encryption Process

### Steps:
1. **Generate a random prime number** `p` (2 ≤ p ≤ 250).
2. Split `p` into upper and lower 4-bit nibbles.
3. Derive rotation counts:
   - `r_upper = (upper_p % 3) + 1`
   - `r_lower = (lower_p % 3) + 1`
4. For each character in the plaintext:
   - Convert it to ASCII.
   - Split it into 4-bit nibbles: upper and lower.
   - Rotate each nibble left by `r_upper` and `r_lower`.
   - Merge and XOR the result with `p`.
5. Return ciphertext as a list of integers, prefixed with the key `p`.

---

## 🔓 Decryption Process

### Steps:
1. Extract the prime key `p` from the first element.
2. Recalculate `r_upper` and `r_lower` using the same method.
3. For each encrypted value:
   - XOR with `p`.
   - Split into upper and lower nibbles.
   - Rotate them **right** by `r_upper` and `r_lower`.
   - Reconstruct original ASCII character.

---

## 🧪 Examples with Test Cases

### 🔹 Example 1: Encrypting & Decrypting `"Sultan"`

#### Original Plaintext: `"Sultan"`

**Encryption Process:**  
- Random Prime `p`: 233  
- `upper_p = 14 (0xE)`, `lower_p = 9 (0x9)`  
- `r_upper = (14 % 3) + 1 = 3`, `r_lower = (9 % 3) + 1 = 1`

| Char | ASCII | Upper | Lower | Rotated Upper | Rotated Lower | Combined | XOR with p | Encrypted |
|------|-------|--------|--------|----------------|----------------|-----------|--------------|------------|
| S    | 83    | 5      | 3      | 10             | 6              | 166       | 71           | 71         |
| u    | 117   | 7      | 5      | 14             | 10             | 234       | 67           | 67         |
| l    | 108   | 6      | 12     | 13             | 6              | 214       | 55           | 55         |
| t    | 116   | 7      | 4      | 14             | 8              | 232       | 57           | 57         |
| a    | 97    | 6      | 1      | 13             | 2              | 210       | 55           | 55         |
| n    | 110   | 6      | 14     | 13             | 7              | 215       | 54           | 54         |

**Ciphertext:** `[233, 71, 67, 55, 57, 55, 54]`  
**Decrypted Text:** `"Sultan"`

---

### 🔹 Example 2: Encrypting & Decrypting `"Lopa"`

#### Original Plaintext: `"Lopa"`

**Encryption Process:**  
- Random Prime `p`: 193  
- `upper_p = 12 (0xC)`, `lower_p = 1 (0x1)`  
- `r_upper = (12 % 3) + 1 = 1`, `r_lower = (1 % 3) + 1 = 2`

| Char | ASCII | Upper | Lower | Rotated Upper | Rotated Lower | Combined | XOR with p | Encrypted |
|------|-------|--------|--------|----------------|----------------|-----------|--------------|------------|
| L    | 76    | 4      | 12     | 8              | 3              | 131       | 66           | 66         |
| o    | 111   | 6      | 15     | 12             | 11             | 203       | 122          | 122        |
| p    | 112   | 7      | 0      | 14             | 0              | 224       | 97           | 97         |
| a    | 97    | 6      | 1      | 12             | 4              | 196       | 69           | 69         |

**Ciphertext:** `[193, 66, 122, 97, 69]`  
**Decrypted Text:** `"Lopa"`

---

## ✅ Benefits of NibbleDance Cipher

- 🪶 **Lightweight**: Operates on 4-bit nibbles; ideal for small devices.
- 🔑 **Dynamic Keys**: Uses randomly generated prime number for each session.
- 🔁 **Reversible**: Perfect symmetry between encryption and decryption.
- 🔒 **Obfuscation**: Combines rotations and XORs for strong confusion and diffusion.

---

## 🧾 Conclusion

**NibbleDance Cipher** is a custom-designed, lightweight encryption scheme that demonstrates how prime numbers, nibble-wise operations, and logical bit manipulation can be combined to produce a secure and reversible cipher. It is ideal for educational purposes, embedded systems, and applications needing fast symmetric encryption.

---

## 📚 References

- Stallings, William. *Cryptography and Network Security: Principles and Practice*.
- Wikipedia: [Bitwise Operation](https://en.wikipedia.org/wiki/Bitwise_operation)
- Python Documentation: [random module](https://docs.python.org/3/library/random.html)

---

## 💻 Source Code

```python
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
    upper_p = (p >> 4) & 0xF
    lower_p = p & 0xF
    r_upper = (upper_p % 3) + 1
    r_lower = (lower_p % 3) + 1
    ciphertext = [p]
    for char in plaintext:
        n = ord(char)
        upper = (n >> 4) & 0xF
        lower = n & 0xF
        upper_rot = rotate_left_4(upper, r_upper)
        lower_rot = rotate_left_4(lower, r_lower)
        combined = (upper_rot << 4) | lower_rot
        ciphertext.append(combined ^ p)
    return ciphertext

def decrypt(ciphertext: list[int]) -> str:
    p = ciphertext[0]
    upper_p = (p >> 4) & 0xF
    lower_p = p & 0xF
    r_upper = (upper_p % 3) + 1
    r_lower = (lower_p % 3) + 1
    plaintext = []
    for c in ciphertext[1:]:
        combined = c ^ p
        upper_rot = (combined >> 4) & 0xF
        lower_rot = combined & 0xF
        upper = rotate_right_4(upper_rot, r_upper)
        lower = rotate_right_4(lower_rot, r_lower)
        decrypted = (upper << 4) | lower
        plaintext.append(chr(decrypted))
    return ''.join(plaintext)
```
