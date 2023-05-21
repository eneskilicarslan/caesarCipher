import collections as col
from collections import Counter
import matplotlib.pyplot as plt
import random

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


def blockCipher(key, texttoCipher, blockSize):
    """
    BLOCK CIPHERING
    :param key:
    :param texttoCipher:
    :param blockSize:
    :return:
    """
    blocks = preProcessADV_ECB(texttoCipher, blockSize)
    cipheredBlocks = xor_key_and_blocks(key, blocks)
    print("key: " + key)
    print("after2: " + cipheredBlocks.__str__())

    return binary_string_to_string(unquantize_blocks(cipheredBlocks))


def blockDecipher(key, cipheredBlocks):
    """
    BLOCK DECIPHERING
    :param key:
    :param cipheredBlocks:
    :return:
    """
    decipheredBlocks = xor_key_and_blocks(key, cipheredBlocks)
    print("deciphered: " + decipheredBlocks.__str__())

    postProcessADV_ECB(decipheredBlocks, len(key))


def preProcessADV_ECB(string, blockSize):
    """
    pre-process for advanced electronic code book block ciphering
    :param string: string to be processed
    :param blockSize: block size to be used
    """
    dataVector = randomBinaryGenerator(blockSize)
    locationVector = randomLocationGenerator(blockSize)
    print("random vector: " + dataVector)
    print("location vector: " + locationVector)
    print("string binary form: " + string_to_binary_string(string))
    quantized = quantize_binary_string(string_to_binary_string(string), blockSize-1)
    print("qunatized: " + quantized.__str__())

    for i in range(len(quantized)):
        for j in range(blockSize):
            if (blockSize == len(quantized[i])) and (locationVector[j] == "1"): #TODO: location vector traversal is a cost, think of location vector as location itself not index
                quantized[i] = add_bit_to_block(quantized[i], j, dataVector[i])

    print("after adding: " + quantized.__str__())
    quantized.insert(0, locationVector)
    quantized.insert(0, dataVector)

    return quantized


def postProcessADV_ECB(blocks, blockSize):
    """
    post-process for advanced electronic code book block ciphering
    :param blocks: blocks to be processed
    :param blockSize: block size to be used
    """
    dataVector = blocks[0]
    locationVector = blocks[1]
    blocks = blocks[2:]
    print("data vector: " + dataVector)
    print("location vector: " + locationVector)
    print("blocks: " + blocks.__str__())

    for i in range(len(blocks)):
        for j in range(blockSize):
            if locationVector[j] == "1":
                blocks[i] = remove_bit_from_block(blocks[i], j)

    print("after removing: " + blocks.__str__())
    return blocks


def xor_key_and_blocks(key, blocks):
    """
    xors key and blocks
    :param key:
    :param blocks:
    :return:
    """
    encrypted_blocks = []
    for block in blocks:
        encrypted_block = "".join(str(int(block_bit) ^ int(key_bit)) for block_bit, key_bit in zip(block, key))
        encrypted_blocks.append(encrypted_block)
    return encrypted_blocks


def add_bit_to_block(block, index, bit):
    """
    adds bit to block at index
    :param block:
    :param index:
    :param bit:
    :return:
    """
    block_list = list(block)
    block_list.insert(index, bit)
    updated_block = ''.join(block_list)
    return updated_block


def remove_bit_from_block(binary_string, index):
    """
    removes bit from block at index
    :param binary_string:
    :param index:
    :return:
    """
    modified_string = binary_string[:index] + binary_string[index+1:]
    return modified_string

def quantize_binary_string(binary_string, block_size):
    """
    quantizes binary string into blocks
    :param binary_string:
    :param block_size:
    :return:
    """
    quantized_blocks = [binary_string[i:i+block_size] for i in range(0, len(binary_string), block_size)]
    return quantized_blocks


def unquantize_blocks(quantized_blocks):
    """
    unquantizes blocks into binary string
    :param quantized_blocks:
    :return:
    """
    binary_string = ''.join(quantized_blocks)
    return binary_string


def string_to_binary_string(input_string):
    """
    converts string to binary string
    :param input_string:
    :return:
    """
    binary_string = ""
    for char in input_string:
        binary_string += bin(ord(char))[2:].zfill(8)
    return binary_string


def binary_string_to_string(binary_string):
    """
    converts binary string to string
    :param binary_string:
    :return:
    """
    string = ""
    for i in range(0, len(binary_string), 8):
        binary_segment = binary_string[i:i+8]
        decimal_value = int(binary_segment, 2)
        character = chr(decimal_value)
        string += character
    return string

def randomBinaryGenerator(length):
    """
    generates random binary string
    :param length: length of the string to be generated
    :return: random binary string
    """
    return ''.join(random.choice('01') for i in range(length))


def randomLocationGenerator(length):
    """
    generates random location
    :param length: length of the string to be generated
    :return: random location
    """
    string_val = "0" * length
    rand = random.randint(0, length-1)
    string_list = list(string_val)
    string_list[rand] = '1'
    modified_string = "".join(string_list)
    return modified_string

