def encrypt(text, shift):
    result = ""

    for char in text:
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)

        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)

        # Leave other characters unchanged
        else:
            result += char

    return result


def decrypt(text, shift):
    # Decryption is simply shifting backwards
    return encrypt(text, -shift)


# ---------------- Main Program ----------------
message = input("Enter your message: ")
shift_value = int(input("Enter shift value (e.g., 3): "))

encrypted_message = encrypt(message, shift_value)
decrypted_message = decrypt(encrypted_message, shift_value)

print("\nEncrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)
