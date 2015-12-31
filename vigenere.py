from collections import defaultdict
def getKey():
    key = input("Please tell me what you wish to use for your key: ")
    key = key.lower()
    return key
def encode():
    alph = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    key = getKey()
    lenKey = len(key)
    message = input("Please enter the message you wish to encode: ")
    lenMessage = len(message)
    i = 0
    j = 0
    encryptMessage = ""
    for i in range(lenMessage):
        messChar = message[i]#extract character from message
        if messChar.isalpha():#check if character is alphabetical, if not, continue loop
            messpos = alph.index(messChar)
            posinkey = j % lenKey #find which position in the keyword we are using during this iteration (clever trick i came up with, as the keyword needs to wrap around and nested for loops suck)
            keyChar = key[posinkey]
            keypos = alph.index(keyChar)
            encryptPosition = messpos + keypos
            encryptKey = alph[encryptPosition]
            encryptMessage += encryptKey
            j += 1
        #finalMessage += messChar #Add this line if you want to include spaces (makes it easier to crack though)
    print(encryptMessage)
    
def decode():
    alph = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    key = getKey()
    lenKey = len(key)
    message = input("Please enter the message you wish to decode: ")
    lenMessage = len(message)
    i = 0
    decryptMessage = ""
    for i in range(lenMessage):
        messChar = message[i]
        messpos = alph.index(messChar)
        posinkey = i % lenKey
        keyChar = key[posinkey]
        keypos = alph.index(keyChar)
        if keypos > messpos:
            messpos += 26
        decryptCharpos = messpos - keypos
        decryptChar = alph[decryptCharpos]
        decryptMessage += decryptChar
    print(decryptMessage)

def main():
    userInput = input("Would you like to encrypt or decrypt code? (e/d): ")
    if userInput[0] == "e" or "E":
        encode()
        userInput2 = input("Would you now like to decode? (y/n): ")
        if userInput2[0] == "y" or "Y":
            decode()
    else:
        decode()

main()