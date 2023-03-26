import collections as col
from collections import Counter
import matplotlib.pyplot as plt


def caesarCipher(textToCipher, key):
    """
    CAESAR CIPHERING
    :param textToCipher: a simple text to be ciphered
    :param key: variable to shift through the alphabet
    :return: ciphered text using key
    """
    # TODO: number ciphering
    cipheredText = ""
    textToCipher.lower()

    for i in range(len(textToCipher)):
        if textToCipher[i] == " ":
            cipheredText += " "
        else:
            cipheredText += chr((ord(textToCipher[i]) + key - 97) % 26 + 97)

    return cipheredText


def freqAnalysis(textToAnalyze, path):
    """
    letter frequency analysis
    :param textToAnalyze: freq analysis will be done over this var
    :return: sorted freq dictionary
    """

    textToAnalyze.lower()
    letterCounts = Counter(textToAnalyze.rstrip())
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
