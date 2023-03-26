import collections as col
import matplotlib.pyplot as plt


def caesarCipher(textToCipher, shift):

    """ CAESAR CIPHERING
    textToCipher: a simple text to be ciphered
    shift: variable to shift through alphabet
    """

    cipheredText = ""
    textToCipher.lower()

    for i in range(len(textToCipher)):
        if textToCipher[i] == " ":
            cipheredText += " "
        else:
            cipheredText += chr((ord(textToCipher[i]) + shift - 97) % 26 + 97)

    return cipheredText



