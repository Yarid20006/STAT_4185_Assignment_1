encrypted_file = open("encrypted_message_two.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Write Code Here

def decrypter(cipher):
    decrypted_message = [''] * len(cipher)
    for i in range(len(cipher)):
        if i % 2 == 0:
            decrypted_message[len(cipher) - i - 1] = cipher[i]
        else:
            decrypted_message[i] = cipher[len(cipher) - i - 1]
    return ''.join(decrypted_message)

with open('encrypted_message_two.txt', 'r') as f:
    encrypted_message = f.read().strip()
    decrypted_message = decrypter(encrypted_message)
    print(decrypted_message)

