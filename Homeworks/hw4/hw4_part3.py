# File:          hw4_part3.py
# Author:        Brendan Cain
# Date:          10/4/16
# Section:       22
# E-mail:        bcain1@umbc.edu
# Description:   Username maker that reprompts user if it doesnt meet 
#                requirements (more requirements than part 1
# Collaboration: Collaboration was not allowed on this assignment.

#valid username is one that is within the character bounds and end in "1" if it
#has less than 8 characters.
def main():
    MIN = 2
    MAX = 8
    #Declare bounds for username as constants.
    name = str(input("Please enter your username: "))
    #gets username from user so it can be checked for validity.
    length = len(name) #stores length of string as a variable (needs updating)
    #enters loop if username is invalid.
    while (length<MAX and name[-1]!="1") or length>MAX or length<MIN:
        #Tells the user whether their entry is too short or too long
        if length<MIN:
            print("That username is too short.")
            print("It must be at least", MIN, "characters long.")
        elif length>MAX:
            print("That username is too long.")
            print("It must be no more than", MAX, "characters long.")
        else:
            print("Usernames under 8 characters must end in '1'.")
        #Prompts the user to enter something else while also updating variables
        name = str(input("Please enter a different username: "))
        length = len(name)
    #End While.
    print("Thank you for choosing the username", name + ".")
#END def main():

main()
