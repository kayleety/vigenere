'''
Kaylee Yin
Cybersecurity - Period 5
October 18, 2020

'''
import sys

#True = encode, False = decode
def vigenere(text, key, code):
    keyLength = len(key)
    index = 0 #index relating to the key
    final = ""

    for i in range(len(text)):
        if code == True: #encode, add letters
            if index == keyLength:
                index = 0
            textIndex = int(ord(text[i]))
            keyIndex = int(ord(key[index])) - 97
            newIndex = textIndex + keyIndex

            if newIndex > 122: #circle back to the beginning of the alphabet
                newIndex -= 26

            index += 1
            final += chr(newIndex)

        if code == False: #decode, subtract letters
            if index == keyLength:
                index = 0
            textIndex = int(ord(text[i]))
            keyIndex = int(ord(key[index])) - 97
            newIndex = textIndex + keyIndex

            if newIndex < 97: #circle to the end of the alphabet
                newIndex -= 26

            index += 1
            final += chr(newIndex)
