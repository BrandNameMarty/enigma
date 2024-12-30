# A journal encryptor and decryptor
import sys

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
        funcType = input("Type E to encrypt and D to decrypt: ")

        # Encryption chosen
        if funcType == "E" or funcType == "e":
            # Loops until valid input type chosen
            while True:
                print("You have chosen to encrypt your journal.")
                textType = input("Type F to input file and T to input text: ")

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
                textType = input("Type F to input file and T to input text.")

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
    print("Enter text, '\\n + endchat' to finish:")

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

def encrypt(text):
    print("encrypt called")

def decrypt(text):
    print("decrypt called")

if __name__ == "__main__":
    main()