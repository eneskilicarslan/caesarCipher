import collections as col
import matplotlib.pyplot as plt


def caesarCipher(textToCipher, key):

    """ CAESAR CIPHERING
    textToCipher: a simple text to be ciphered
    key: variable to key through alphabet
    """

    cipheredText = ""
    textToCipher.lower()

    for i in range(len(textToCipher)):
        if textToCipher[i] == " ":
            cipheredText += " "
        else:
            cipheredText += chr((ord(textToCipher[i]) + key - 97) % 26 + 97)

    return cipheredText



