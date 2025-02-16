def encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():    
            start = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - start + shift) % 26 + start)
            encrypted_message += encrypted_char
        else:    
            encrypted_message += char
    
    return encrypted_message

def decrypt(message, shift):
    decrypted_message = ""
     
    for char in message:
        if char.isalpha():          
            start = 65 if char.isupper() else 97
            decrypted_char = chr((ord(char) - start - shift) % 26 + start)
            decrypted_message += decrypted_char
        else:      
            decrypted_message += char
    return decrypted_message

def main():
    
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
     
    encrypted_message = encrypt(message, shift)
    print(f"Encrypted message: {encrypted_message}")
  
    decrypted_message = decrypt(encrypted_message, shift)
    print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()