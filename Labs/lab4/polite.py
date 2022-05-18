# File Name:     polite.py
# Author:        Brendan Cain
# Date:          09/28/16
# Section:       22
# E-mail:        bcain1@umbc.edu
# Description:   Program that decides whether user has manners
# Collaboration: During lab, collaboration between students is allowed,
#                although I understand I still must understand the material
#                and complete the assignment myself.

def main():
    
    word = str(input("Please enter a word: "))
    
    #Checks to see if the word is mannerly and then responds accordingly.
    if word == 'please' or word == 'thanks' or word == 'pardon' :
        print("Your manners are impeccable!")
    else :
        print("How utterly rude!")

#END def main():

main()
