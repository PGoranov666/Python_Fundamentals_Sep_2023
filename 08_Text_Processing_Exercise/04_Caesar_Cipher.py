message = input()
encrypt_message = ""

for character in message:
    encrypted_character = chr(ord(character) + 3)
    encrypt_message += encrypted_character
print(encrypt_message)
