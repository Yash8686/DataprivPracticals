import hashlib

def sha256_hash(password):
    # Encode the password to bytes, then compute SHA-256 hash
    hash_object = hashlib.sha256(password.encode())

    # Return hexadecimal representation
    return hash_object.hexdigest()


# -------- Main Program --------
password = input("Enter password: ")
hashed_value = sha256_hash(password)

print("SHA-256 Hashed Value:", hashed_value)
