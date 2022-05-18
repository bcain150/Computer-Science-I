# File:          hw4_part1.py
# Author:        Brendan Cain
# Date:          10/3/16
# Section:       22
# E-mail:        bcain1@umbc.edu
# Description:   Username maker that reprompts user if it doesnt meet 
#                requirements (between 4 and 12 characters long).
# Collaboration: Collaboration was not allowed on this assignment.

def main():
    MIN = 4
    MAX = 12
    #Declare bounds for username as constants.
    name = str(input("Please enter your username: "))
    #gets username from user and stores it so that we can check it.
    #enters loop if username is invalid.
    while len(name) < MIN or len(name) > MAX :
        #Tells the user whether their entry is too short or too long
        if len(name) < MIN :
            print("That username is too short.")
        else :
            print("That username is too long.")
        #Prompts the user to enter something else.
        print("The username must be between", MIN, "and", MAX, "characters.")
        name = str(input("Please enter a different username: "))
    #End While.
    print("Thank you for choosing the username", name + ".")
#END def main():

main()
