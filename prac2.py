def encrypt_rail_fence(text, key):
    rail = [['\n' for _ in range(len(text))]
                     for _ in range(key)]

    # Determine the direction
    down = False
    row, col = 0, 0

    for char in text:
        # Change direction on hitting top or bottom rail
        if row == 0 or row == key - 1:
            down = not down

        rail[row][col] = char
        col += 1

        # Move row
        row = row + 1 if down else row - 1

    # Construct encrypted text
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])

    return "".join(result)


def decrypt_rail_fence(cipher, key):
    rail = [['\n' for _ in range(len(cipher))]
                     for _ in range(key)]

    # Mark positions with '*'
    down = None
    row, col = 0, 0

    for _ in cipher:
        if row == 0:
            down = True
        elif row == key - 1:
            down = False

        rail[row][col] = '*'
        col += 1
        row = row + 1 if down else row - 1

    # Fill the marked positions with characters
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    # Read message zig-zag
    result = []
    row, col = 0, 0
    for _ in cipher:
        if row == 0:
            down = True
        elif row == key - 1:
            down = False

        if rail[row][col] != '\n':
            result.append(rail[row][col])
            col += 1

        row = row + 1 if down else row - 1

    return "".join(result)


# -------------- Main Program --------------
message = input("Enter message: ")
key = int(input("Enter number of rails: "))

encrypted = encrypt_rail_fence(message, key)
decrypted = decrypt_rail_fence(encrypted, key)

print("\nEncrypted Message:", encrypted)
print("Decrypted Message:", decrypted)
