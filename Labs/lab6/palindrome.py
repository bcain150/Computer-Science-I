# File:          palindrome.py
# Author:        Brendan Cain
# Date:          10/12/16
# Section:       22
# E-mail:        bcain1@umbc.edu
# Description:   takes in word and checks to see if it is a palindrome
# Collaboration: During lab, collaboration between students is allowed,
#                although I understand I still must understand the material
#                and complete the assignment myself. 

def main():
    #takes in a string from the user.
    pal = str(input("Enter a word: "))
    backWord = ""
    #reverses the users input string.
    for i in range(len(pal)-1, -1, -1):
        backWord += pal[i]
    #END for
    #Checks to see if the reversed word = the original word
    if pal == backWord:
        print(pal, "is a palindrome.")
    else:
        print(pal, "is not a palindrome.")
#END def main():

main()
