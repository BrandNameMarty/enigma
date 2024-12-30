# Creating a journal encryptor / decryptor
import sys

def main():
    while True:
        funcType = input("Type E to encrypt and D to decrypt: ")

        if funcType == "E":
            while True:
                print("You have chosen to encrypt your journal.")
                textType = input("Type F to input file and T to input text.")

                if textType == "F":
                    text = inputFile()
                    break
                elif textType == "T":
                    text = inputText()
                    break
                else:
                    print("Invalid, please try again.")

            encrypt(text)
            break

        elif funcType == "D":
            while True:
                print("You have chosen to decrypt your journal.")
                textType = input("Type F to input file and T to input text.")

                if textType == "F":
                    text = inputFile()
                    break
                elif textType == "T":
                    text = inputText()
                    break
                else:
                    print("Invalid, please try again.")

            decrypt(text)
            break

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