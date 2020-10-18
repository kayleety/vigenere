'''
Kaylee Yin
Cybersecurity - Period 5
October 18, 2020

'''
import sys

#True = encode, False = decode
def vigenere(text, key, code):
    text = text.upper() #make all characters uppercase
    for i in text: #ensure only capitalized letters are included
        if ord(i) < 65 or ord(i) > 90:
            text = text.replace(i, "")

    keyLength = len(key)
    index = 0 #index relating to the key
    final = ""

    for i in range(len(text)):
        if index == keyLength:
            index = 0
        textIndex = int(ord(text[i]))
        keyIndex = int(ord(key[index])) - 65

        if code == True:
            newIndex = textIndex + keyIndex
            if newIndex > 90: #circle back to the beginning of the alphabet
                newIndex -= 26

        else:
            newIndex = textIndex - keyIndex
            if newIndex < 65: #circle to the end of the alphabet
                newIndex = 26 + (textIndex - keyIndex)

        index += 1
        final += chr(newIndex)

        '''
        if code == True: #encode, add letters
            if index == keyLength:
                index = 0
            textIndex = int(ord(text[i]))
            keyIndex = int(ord(key[index])) - 65
            newIndex = textIndex + keyIndex

            if newIndex > 90: #circle back to the beginning of the alphabet
                newIndex -= 26

            index += 1
            final += chr(newIndex)

        if code == False: #decode, subtract letters
            if index == keyLength:
                index = 0
            textIndex = int(ord(text[i]))
            keyIndex = int(ord(key[index])) - 65
            newIndex = textIndex - keyIndex

            if newIndex < 65: #circle to the end of the alphabet
                newIndex = 26 + (textIndex - keyIndex)

            index += 1
            final += chr(newIndex)
        '''
    print(final)

vigenere('hotdogstand', 'BOAR', True) #test code
