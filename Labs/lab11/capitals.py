# File:    capitals.py
# Started: by Dr. Gibson
# Author:  Brendan Cain
# Date:    11/16/16
# Section: 22
# E-mail:  bcain1@umbc.edu
# Description:
#   This file contains python code that reads in a list of
#   states and their capitals, stores it in a dictionary,
#   and then allows the user to list all options (states),
#   or to show the capital of a specified state.
# Collaboration: During lab, collaboration between students is allowed,
#                although I understand I still must understand the material
#                and complete the assignment myself. 

QUIT     = "exit"
SHOW_ALL = "list"

# convertToDict() takes in the filename and converts to a dict
# Input:          a file object
# Output:         a dictionary containing the file contents
def convertToDict(fileContents):
    dict1 = {}
    # write the rest of the function (including the return)
    
    #read in the states and capitals
    stateList = fileContents.readlines()
    for s in stateList:
        #splits up states and capitals
        stateCap = s.split(',')
        state = stateCap[0]
        capital = stateCap[1]
        #adds to dictionary
        dict1[state] = capital
    #end for
    return dict1

#end def converToDict()

def main():

    stateCapFile = open("stateCaps.txt")
    # a function call to convertToDict goes here
    stateCapDict = convertToDict(stateCapFile)
    
    stateCapFile.close()

    print("Welcome to the State Capital Lookup System")
    # message with all the prompts for the user
    msg = "\n\tPlease enter the state you want the capital of.\n" + \
        "\t(Use '" + SHOW_ALL + "' for choices, or '" + \
        QUIT + "' to quit): "

    choice = input(msg)

    # this should be a while loop that runs until the user chooses to "exit"
    # MAKE SURE TO USE THE CONSTANTS DEFINED AT THE TOP OF THE FILE!!!
    while choice != QUIT:
        # inside the loop: if the user enters "list", show all the states
        if choice == SHOW_ALL:
            for state in stateCapDict.keys():
                print(state)
        # inside the loop: otherwise; check if the state exists
        elif choice in stateCapDict.keys():
            # if the state exists, print its capital
            print(stateCapDict[choice])
            # otherwise, print that it is not a state
        else:
            print("That is not a state!")
        # at the end of the while loop, get a new user input
        choice = input(msg)
    #end while
    print("Thank you for using the State Capital Lookup System!")
#end def main():

main()

    

