def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26
            result += chr(shifted + base)
        else:
            result += char 
    return result
def decrypt(text, shift):
    return encrypt(text, -shift) 
user_text = input("Enter text to encrypt: ")
shift_key = int(input("Enter shift key (e.g. 3): "))
encrypted = encrypt(user_text, shift_key)
decrypted = decrypt(encrypted, shift_key)
print(f"\nOriginal:  {user_text}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")