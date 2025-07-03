def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - start + shift * mode) % 26 + start)
            result += shifted_char
        else:
            result += char
    return result

def encrypt(text, shift):
    return caesar_cipher(text, shift, 1) # mode 1 for encryption

def decrypt(text, shift):
    return caesar_cipher(text, shift, -1) # mode -1 for decryption

# Get input from user
message = input("Enter your message: ")
shift_value = int(input("Enter the shift value: "))
operation = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()

if operation == 'e':
    encrypted_message = encrypt(message, shift_value)
    print("Encrypted message:", encrypted_message)
elif operation == 'd':
    decrypted_message = decrypt(message, shift_value)
    print("Decrypted message:", decrypted_message)
else:
    print("Invalid operation. Please choose 'e' for encrypt or 'd' for decrypt.")