import sys

file = input("Add file path that you would like to submit as a solution: ")
url = input("Add url that you would like to submit to: ")
description = input("Describe the program that we made here: ")

## Simple do while loop in python. Conditional is the except statement.
## If error raised, continue looping. If not, end looping.

while True:
    try:
        
        with open(file, 'r') as f:
            text = f.read()
            
    except OSError:
        file = input("Could not open file. Please enter file path again: ")
        continue
    break

## Add four spaces to all of the from the file.
text = "    " + text.replace("\n","\n    ")

text = description + "\n " + text
text = "Python Version: " + str(sys.version[:5])+ "\n" + "\n" + text

print(text)
