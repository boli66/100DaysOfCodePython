import assets
from libraries import ASCII
ASCII.printLogo("Logo.txt")
def encrypt(message, shift):
    message = str(message)
    message.lower()
    encrypted = ""
    for i in message:
        try:
            index = assets.alphabet.index(i)
        except ValueError:
            encrypted += i
            continue
        index+=shift
        while index > len(assets.alphabet)-1:
            index -= len(assets.alphabet)
        encrypted+= assets.alphabet[index]

    return encrypted

def decrypt(message, shift):
    message = str(message)
    message.lower()
    decrypted = ""
    for i in message:
        try:
            index = assets.alphabet.index(i)
        except ValueError:
            decrypted += i
            continue
        index-=shift

        while(index < 0):
            index+=len(assets.alphabet)
        decrypted+= assets.alphabet[index]

    return decrypted

while True:
    direction = input('Type "encode" to encrypt a message and type "decode" to decrypt a message:\n')
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    s = ""
    if(direction.lower() == "encode" or direction.lower() == "e"):
        s = encrypt(text,shift)
    else:
        s = decrypt(text,shift)
    print(f"The message is now:{s}")
    s = input("Do you want to go again [Y/n]?: ")
    if(s.lower() != "y"):
        print("Bye")
        break
    else:
        print("")
