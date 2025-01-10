# This file acts as scaffolding for the work being done in the other files.

# Imports
from input import chooseFunc, inputFile, inputText
from encrypt import encrypt
from decrypt import decrypt

"""
The skeleton function for the journal encryptor / decryptor.
Prompts the user to choose to encrypt or decrypt.
Then prompts the user to choose to input a file or raw text.
Will create a newly encrypted or decrypted .txt file with a new name.
"""
def main():
    # Print header
    header()
    
    # Allow the user to choose the function and input type
    funcType, inputType = chooseFunc()

    # Get text input
    text = inputFile() if inputType == "f" else inputText()

    # Call encrypt or decrypt and store created file name
    fileName = encrypt(text) if funcType == "e" else decrypt(text)
    print(f"filename={fileName}")

    # Print footer
    footer(funcType, fileName)

"""
Printing preliminary application information.
"""
def header():
    print("Welcome to Enigma!")
    print("This application is a journal encryptor and decryptor.")
    print("To navigate this app, simply use keyboard inputs when prompted.")
    print("Created by Marty Brandwein, 2025.\n")

"""
Printing post-application message.
Takes as input type of function and name of returned file
"""
def footer(funcType, fileName):
    funcType = "encrypted" if funcType == "e" else "decrypted"
    print(f"\nYour text was successfully {funcType} and is now stored in {fileName}.")
    print("Have a great day <3")

if __name__ == "__main__":
    main()