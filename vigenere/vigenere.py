'''
Kaylee Yin
Cybersecurity - Period 5
October 18, 2020

'''
import sys

def vigenere(text, key, code):
    text = text.upper() #make all characters uppercase
    for i in text: #ensure only capitalized letters are included
        if ord(i) < 65 or ord(i) > 90:
            text = text.replace(i, "")

    keyLength = len(key)
    index = 0 #index relating to the key
    final = ""

    for i in range(len(text)): #go through every letter in text
        if index == keyLength:
            index = 0
        textIndex = int(ord(text[i]))
        keyIndex = int(ord(key[index])) - 65 #letter correlates w/ # place in alphabet

        if code == "encode":
            newIndex = textIndex + keyIndex #encode => add
            if newIndex > 90:
                newIndex -= 26 #circle back to the beginning of the alphabet

        else:
            newIndex = textIndex - keyIndex #decode => subtract
            if newIndex < 65:
                newIndex = 26 + (textIndex - keyIndex) #circle to the end of the alphabet

        index += 1
        final += chr(newIndex) #add to final text to be printed

    print(final)

if __name__ == "__main__":
    code = sys.argv[1]
    text = sys.argv[2]
    key = sys.argv[3]
    vigenere(text, key, code)
