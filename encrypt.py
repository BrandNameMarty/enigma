# This file handles the encryption of the inputted text.

import random
import sys

# Global variables for this file
asciiChars = ''.join(chr(i) for i in range(32, 127))

"""
Generate a new ASCII key.
"""
def generateKey():
    asciiList = list(asciiChars)
    random.shuffle(asciiList)
    return ''.join(asciiList)

"""
If the key does not yet exist in the file, write it in.
Expects key --> some ASCII string to be saved as a key.
"""
def saveKey(key):
    try:
        with open("keys.txt", "a") as file:
            file.write(key + "\n")
    except Exception as e:
            print(f"Failed to create keys file: {e}")
            sys.exit(1)

"""
Finds and returns the index of the key in keys.txt.
Returns the index the key is found at, or will be stored at, and a boolean 
signifying if the key already exists in keys.txt.
If keys.txt does not yet exist, return -1 and False.
"""
def findKeyIndex(key):
    # Try to read and see if randAscii already exists in the keys
    try:
        # Read keys and split them by new line
        with open("keys.txt", 'r') as file:
            keys = file.read()
        keys.split("\n")

        # See if randAscii already exists in keys
        for k in keys:
            if k == key:
                break
            index += 1
        
        # If key does not yet exist, return index where it will be stored and
        # that it does not yet exist
        if index == len(keys):
            return index, False

        # Return index of key and that it exists
        return index, True
    
    except FileNotFoundError: # If file does not yet exist
        return -1, False

"""
Encrypts inputted text using a generated key.
Expects as input a string to be encrypted.
Returns the encrypted text and the index of its key.
"""
def encrypt(text):
    # Generate new key and check if it is in keys.txt already
    key = generateKey()
    index, exists = findKeyIndex(key)

    # Save key to keys.txt if it does not yet exist and store its index
    if exists == False:
        saveKey(key)
        index = 0 if index == -1 else index

    # Mapping ASCII values to shuffled values
    keyDict = {key: value for key, value in zip(asciiChars, key)}

    # Encrypting text with first line representing the index of the key
    encrypted = "".join(keyDict.get(c, c) for c in text)