# This file handles the user's preliminary selections.

import sys

"""
Prompts the user to choose to encrypt or decrypt their text. Calls chooseInput
to prompt user to choose to input file or text.
Returns funcType, inputType where funcType = "e" for encrypt or "d" for decrypt
and inputType = "f" for file and "t" for text.
"""
def chooseFunc():
    # Valid types of functions to select
    validFuncs = ["E", "e", "D", "d"]

    try:
        # Prompt for function type
        funcType = input("Type E to encrypt or D to decrypt: ")

        # funcType is valid
        if funcType in validFuncs:
            inputType = chooseInput()

             # Return the function and input selection
            return funcType.lower(), inputType

        # Invalid funcType, retry
        print("Invalid function, please try again.")
        chooseFunc()

    # Catch KeyboardInterrupt
    except KeyboardInterrupt:
        print("Keyboard interrupted.")
        sys.exit(1)

"""
Helper function for chooseFunc(), prompts the user to choose the type of text
input.
Returns "f" is file input is chosen and "t" if text input is chosen.
"""
def chooseInput():
    # Valid types of inputs to select
    validInputs = ["F", "f", "T", "t"]

    try:
        # Prompt for input type
        inputType = input("Type F to input file and T to type in text: ")

        # inputType is valid
        if inputType in validInputs:
            return inputType.lower()

        # Invalid funcType, retry
        print("Invalid input, please try again.")
        chooseInput()

    except KeyboardInterrupt:
        print("Keyboard interrupted.")
        sys.exit(1)

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