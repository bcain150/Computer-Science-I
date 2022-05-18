# File:          hw7.py
# Author:        Brendan Cain
# Date:          11-1-16
# Section:       22
# E-mail:        bcain1@umbc.edu
# Description:   uses 6 functions to implement a simple list checker prgm.
# Collaboration: I did not collaborate with anyone on this assignment.

# createIntList() creates a list of integers by prompting the user in a loop
# Input: The sentinel value as an integer for the loop
# Output: The list of integers.

def createIntList(SENT):
    
    #initiates the prompt string, the first entry and the return list.
    PROMPT = "Please enter a number, " + str(SENT) + " to stop: "
    num = int(input(PROMPT))
    intList = []
    #While loop with sentinel in parameter
    while num != SENT:
        intList.append(num)
        num = int(input(PROMPT))
    #END while
    return intList

#END def createIntList():

# getValidInt() loops until the user enters a number within the min and max
# Input: min and max parameters
# Output: the valid int entered by the user

def getValidInt(minn, maxx):
    
    #initiate the prompt string and the first attempt.
    PROMPT = "Please enter a number between " + str(minn) + " and " + str(maxx)+ " (inclusive): "
    entry = int(input(PROMPT))
    #While loop to check if entry is within parameters if it's not, reprompt
    
    while entry < 1 or entry > 5:
        entry = int(input(PROMPT))
    #end while
    return entry
#End def getValidInt():

# printMenu() prints out menu options for the user using constants
# Input: none
# Output: none

def printMenu():
    
    #initiates choices as Constants
    PICK1 = "1 - Create a list"
    PICK2 = "2 - Check if list is all same"
    PICK3 = "3 - Check if list is all different"
    PICK4 = "4 - Check if list is sorted"
    PICK5 = "5 - Exit the program"
    #prints constants
    print("Please make a choice from the menu: ")
    print(PICK1)
    print(PICK2)
    print(PICK3)
    print(PICK4)
    print(PICK5)
    print()
#end def printMenu():

# allTheSame() true if all elements in a list are =. otherwise it is false
# Input: a list
# Output: returns true or false

def allTheSame(aList):
    
    #for loop that goes through every index except the last one
    for i in range(len(aList)-1):
        #tests if the value in that index is in the slice ahead of it
        test = aList[i]
        if test not in aList[i+1:]:
            #returns false if the test is not in the slice
            return False
    #in the case that the if statement is always false... the func retuns true
    return True
#End def allTheSame():

# allDifferent() true if all elements in a list are !=. otherwise it is false
# Input: a list
# Output: returns true or false

def allDifferent(aList):
    #for loop that goes through every index except the last one
    for i in range(len(aList)-1):
        #tests if the value in that index is in the slice ahead of it
        test = aList[i]
        if test in aList[i+1:]:
            #returns false if the test is in the slice
            return False
    #in the case that the if statement is always false... the func retuns true
    return True

#End def allDifferent():

# sorted() true if the elements in the list got from least to greatest
# Input: a list
# Output: returns true or false

def sorted(aList):
    
    #for loop to go through the entire list except last index becaue of 'if'
    for i in range(len(aList)-1):
        #checks to see if there is an index "out of order"
        if aList[i] > aList[i+1]:
            return False
    #otherwise, return true
    return True

#end def sorted():

def main():
    MIN = 1
    MAX = 5
    #print the menu
    theList = []
    printMenu()
    pick = getValidInt(MIN, MAX)
    #The main menu loop
    while pick != 5:
        #Each statement checks to see what choice was made
        if pick == 1: #Create a List
            sent = int(input("What do you want your sentinel to be? "))
            theList = createIntList(sent)
        
        elif pick == 2: #all the same
            #calls all the same and checks it then prints out return msg.
            ans = allTheSame(theList)
            if ans:
                print("The list", theList, "is all the same element.")
            else:
                print("The list", theList, "is not all the same element.")
        
        elif pick == 3: #all different
            #calls all different and checks it then prints out return msg.
            ans = allDifferent(theList)
            if ans:
                print("The list", theList, "are all unique elements.")
            else:
                print("The list", theList, "are not all unique elements.")
        
        else: #pick must == 4 therefore go to see if there are in order.
            #calls sorted() and outputs respectively
            ans = sorted(theList)
            if ans:
                print("The list", theList, "is sorted.")
            else:
                print("The list", theList, "is not sorted.")
        #END if statements
        print(("-"*5 + " ")*6)
        print()
        printMenu()
        pick = getValidInt(MIN,MAX)
    #END WHILE

    print("Thank you for using The List Info Checker.")
#END def main():

main()
