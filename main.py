# A journal encryptor and decryptor
import random

# Defining global variables
asciiChars = ''.join(chr(i) for i in range(32, 127))
fileName = ""

"""
The skeleton function for the journal encryptor / decryptor.
Prompts the user to choose to encrypt or decrypt.
Then prompts the user to choose to input a file or raw text.
Will return a newly encrypted or decrypted .txt file with a corresponding
file name (ex: journal.txt --> encrypted_journal.txt).
"""
def main():
    # Loops until valid function type is chosen
    while True:
        # Prompt for function type
        funcType = input("Type E to encrypt or D to decrypt: ")

        # Encryption chosen
        if funcType == "E" or funcType == "e":
            # Loops until valid input type chosen
            while True:
                print("You have chosen to encrypt your journal.")
                textType = input("Type F to input file or T to input text: ")

                # File input chosen
                if textType == "F" or textType == "f":
                    inText = inputFile()
                    break

                # Text input chosen
                elif textType == "T" or textType == "t":
                    inText = inputText()
                    break

                # Invalid input, try again
                else:
                    print("Invalid, please try again.")

            # Run encryption on input
            if inText:
                encrypt(inText)

            # End script
            break

        # Decryption chosen
        elif funcType == "D" or funcType == "d":
            # Loops until valid input type chosen
            while True:
                print("You have chosen to decrypt your journal.")
                textType = input("Type F to input file or T to input text.")

                # File input chosen
                if textType == "F" or textType == "f":
                    inText = inputFile()
                    break

                # Text input chosen
                elif textType == "T" or textType == "t":
                    inText = inputText()
                    break

                # Invalid input, try again
                else:
                    print("Invalid, please try again.")

            # Run decryption on input
            if inText:
                decrypt(inText)
            
            # End script
            break

        # Invalid function type, retry
        else:
            print("Invalid, please try again.")

"""
Prompts user to input text version of a journal to encrypt or decrypt.
Processes inputted text until 'endchat' line is inputted.
Returns a string representing the entire journal or None if script ended.
"""
def inputText():
    # Init array of lines
    lines = []

    # Prompt user to enter text
    print("Enter text, 'endchat + \\n' to finish:")

    # Read user's inputted lines
    try:
        # Loops until input is terminated
        while True:
            line = input()

            # Terminate input
            if line == "endchat":
                if lines:
                    print("\nInput terminated.")
                    separator = "\n"
                    journal = separator.join(lines)
                    break
                
                # If nothing was inputted, keyboard interrupt
                else:
                    raise KeyboardInterrupt
            
            # Input not terminated, read line and continue
            lines.append(line)

    # KeyboardInterrupt caught, respond accordingly
    except KeyboardInterrupt:
        # If lines have been read, inform user of final line loss
        if lines:
            print("\nInput stopped. Final line potentially lost. You typed:\n")
            print("\n".join(lines))
            while True:
                proceed = input("Would you like to proceed (P) or retry (R)?")
                if proceed == "P":
                    separator = "\n"
                    journal = separator.join(lines)
                    break
                elif proceed == "R":
                    inputText()
                else:
                    print("Invalid decision, please try again.")
        
        # If no lines read, end script
        else:
            print("\nNothing was inputted...")
            journal = None

    return journal

"""
Prompts user to input file version of a journal to encrypt or decrypt.
Processes inputted file.
Returns a string representing the entire journal.
"""
def inputFile():
    # Loops until file is successfully read
    while True:
        try:
            # Prompt user for a file name or path
            file_path = input("Enter the file path to open: ")

            # Open the file in read mode
            with open(file_path, 'r') as file:
                journal = file.read()
                fileName = file_path
            
            break

        except FileNotFoundError:
            print("File not found. Please check the path and try again.")
            journal = None
            continue

        except Exception as e:
            print(f"An error occurred: {e}")
            raise KeyboardInterrupt

        except KeyboardInterrupt:
            journal = None
            break

    return journal

"""
Encrypts inputted text, prepending a number that corresponds to some cryptic key.
Expects as input a string to be encrypted.
Creates an encrypted file with corresponding name (ex: journal.txt --> encrypted_journal.txt).
"""
def encrypt(text):
    randAscii = str(random.shuffle(list(asciiChars)))
    index = 0

    # Try to read and see if randAscii already exists in the keys
    try:
        # Read keys and split them by new line
        with open("keys.txt", 'r') as file:
            keys = file.read()
        keys.split("\n")

        # See if randAscii already exists in keys
        for key in keys:
            if key == randAscii:
                break
            index += 1

        # randAscii does not yet exist
        if index == len(keys):
            raise FileNotFoundError
    
    except FileNotFoundError: # If file does not yet exist
        try:
            with open("keys.txt", 'w') as file:
                file.write(f"{randAscii}\n")

        except Exception as e:
            print(f"Failed to create keys file: {e}")

    # randAscii is now logged in keys @ index

    # Mapping ASCII values to shuffled values
    keyDict = {key: value for key, value in zip(asciiChars, randAscii)}

    # Encrypting text with first line representing the index of the key
    encrypted = f"{index}\n"
    for c in text:
        n = keyDict[c]
        encrypted = f"{encrypted}n"

    # Creating new encrypted file using given name
    
    # If no file name yet given, ask for one
    if fileName == "":
        fileName = input("Name your new file: ")

    with open(f"encrypted_{fileName}", 'w') as file:
        file.write(encrypted)

def decrypt(text):
    print("decrypt called")

if __name__ == "__main__":
    main()