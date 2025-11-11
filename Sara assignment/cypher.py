def encrypt(shift, message):
    encrypted_text = ""

    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text += new_char
        else:
            encrypted_text += char

    return encrypted_text


def decrypt(shift, message):
    return encrypt(-shift, message)


def main():
    message = input("Please type the message you want to encrypt or decrypt: ")

    e_or_d = input("Do you want to encrypt or decrypt your message? (encrypt/decrypt or e/d): ").lower()

    while e_or_d not in ["encrypt", "decrypt", "e", "d"]:
        print("Error! Please type encrypt, decrypt, e, or d.")
        e_or_d = input("Do you want to encrypt or decrypt your message? (encrypt/decrypt or e/d): ").lower()

    
    while True:
        try:
            shift = int(input("What is the shift your message uses? "))
            break
        except ValueError:
            print("Error! Please enter a NUMBER for the shift.")
    
    if e_or_d in ["encrypt", "e"]:
        final_msg = encrypt(shift, message)
    else:
        final_msg = decrypt(shift, message)
    print("\n✅ Result:", final_msg, "\n")


main()
