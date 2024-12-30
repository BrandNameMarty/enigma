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
        if funcType == "E":
            # Loops until valid input type chosen
            while True:
                print("You have chosen to encrypt your journal.")
                textType = input("Type F to input file and T to input text.")

                # File input chosen
                if textType == "F":
                    inType = inputFile()
                    break

                # Text input chosen
                elif textType == "T":
                    inType = inputText()
                    break

                # Invalid input, try again
                else:
                    print("Invalid, please try again.")

            # Run encryption on input
            encrypt(inType)
            break

        # Decryption chosen
        elif funcType == "D":
            # Loops until valid input type chosen
            while True:
                print("You have chosen to decrypt your journal.")
                textType = input("Type F to input file and T to input text.")

                # File input chosen
                if textType == "F":
                    inType = inputFile()
                    break

                # Text input chosen
                elif textType == "T":
                    inType = inputText()
                    break

                # Invalid input, try again
                else:
                    print("Invalid, please try again.")

            # Run decryption on input
            decrypt(inType)
            break

        # Invalid function type, retry
        else:
            print("Invalid, please try again.")

def inputText():
    lines = []
    print("Enter text, 'endchat' to finish:")

    try:
        while True:
            line = input()

            if line == "endchat":
                if lines:
                    print("\nInput stopped. You typed:\n")
                    print("\n".join(lines))
                else:
                    print("\nNothing was inputted...")
                
                break
                    
            lines.append(line)

    except KeyboardInterrupt:
        if lines:
            print("\nInput stopped. Final line potentially lost. You typed:\n")
            print("\n".join(lines))
        else:
            print("\nNothing was inputted...")

def inputFile():
    print("inputFile called")

def encrypt():
    print("encrypt called")

def decrypt():
    print("decrypt called")

if __name__ == "__main__":
    main()