from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

#Password Hashing function and producing an Argon2 hash.
def hash_password(password: str) -> str:
    return password_hash.hash(password)

# verification during login password
# Do not decrypt the stored hash
def verify_password(password: str, hashed_password: str) -> bool:
    return password_hash.verify(password, hashed_password)

