import collections as col
from collections import Counter
import matplotlib.pyplot as plt

alphabet = "abcçdefgğhıijklmnoöpqrsştuüvwxyz0123456789"


def caesarCipher(textToCipher, key):
    """
    CAESAR CIPHERING
    :param textToCipher: a simple text to be ciphered
    :param key: variable to shift through the alphabet
    :return: ciphered text using key
    """

    cipheredText = ""
    textToCipher = textToCipher.lower()

    for i in range(len(textToCipher)):
        if textToCipher[i] == " ":
            cipheredText += " "
        elif textToCipher[i] in alphabet:
            idx = (alphabet.index(textToCipher[i]) + key) % len(alphabet)
            cipheredText += alphabet[idx]
        else:
            cipheredText += textToCipher[i]

    return cipheredText


def decipherZipped(textToDecipher, decipherDict):
    """
    deciphering according to decipherDict
    :param textToDecipher:
    :param decipherDict:
    :return: deciphered Text
    """

    decipheredText = ""
    for i in range(len(textToDecipher)):
        if textToDecipher[i] == " ":
            decipheredText += " "
        elif textToDecipher[i] not in alphabet:
            decipheredText += textToDecipher[i]
        else:
            decipheredText += decipherDict[textToDecipher[i]]

    return decipheredText


def compareFreqs(cipherFreq, analysisFreq):
    """
    comparing two analysis between each other to zip
    :param cipherFreq:
    :param analysisFreq:
    :return: zipped dictionary
    """
    decipherDict = {}

    for (char1, char2) in zip(analysisFreq, cipherFreq):
        decipherDict[char2] = char1

    return decipherDict


def freqAnalysis(textToAnalyze, path):
    """
    letter frequency analysis
    :param textToAnalyze: freq analysis will be done over this var
    :return: sorted freq dictionary
    """
    # TODO: will space character be added? if not, create an exception here
    textToAnalyze = textToAnalyze.lower()
    letterCounts = Counter(textToAnalyze.rstrip())
    del letterCounts[' ']
    sortedLetterCounts = col.OrderedDict(sorted(letterCounts.items(), key=lambda t: t[1], reverse=True))
    toGraph(sortedLetterCounts).savefig(path, bbox_inches='tight', transparent=True)

    return sortedLetterCounts


def toGraph(sortedLetterCounts):
    plt.clf()
    plt.bar(list(sortedLetterCounts.keys()), sortedLetterCounts.values(), color='black')
    plt.xlabel("karakter")
    plt.ylabel("frekans")
    ax = plt.gca()
    ax.set_facecolor('#F0F0F0')
    return plt


def intervalBetween(string1, string2):
    return sum(string1[i] != string2[i] for i in range(len(string1)))

