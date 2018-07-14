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
        print(file)
        file = input("Could not open file. Please enter file path again: ")
        continue
    break

## Add four spaces to all of the from the file.
text = "   " + text.replace("\n","\n    ")

## Loop until the user enters a proper description.
while type(description) != str:
    description = input("You did not enter a description. Please enter one now: ")

## TODO: ensure that the url entered is proper.
    
## Add description to the text and put programming version and language at
## the end. 
text = description + "\n " + text
text = "Python Version: " + str(sys.version[:5])+ "\n" + "\n" + text

## Add disclaimer at the end of the comment about this comment.
disclaimer = " This comment was made with a simple script that I use. If there are any problems or issues, feel free to let me know! And if you'd like to see the code, visit my github page here: https://github.com/zicameau/dailyProgrammerPostingAndFormatting"

disclaimer = disclaimer.replace(" ", " ^")

text = text + "\n \n" + disclaimer

print(text)
