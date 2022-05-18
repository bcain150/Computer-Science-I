# File: hw6.py
# Author: Brendan Cain
# Date: 10/24/16
# Section: 22
# E-mail: bcain1@umbc.edu
# Description: contains 4 different functions that are used in main
# Collaboration: collaboration is not allowed on this assignment


# summation() calculates the sum of numbers
# input:      a list of integers or the things you wish to sum
# outputs:    the sum of the list
def summation(aList):
    #initiate the total to start at zero and uses a for loop to add each number
    total = 0
    for num in aList:
        total += num
    #outputs total
    return total
#end def summation():


# multiply()  calculates the product of numbers
# input:      a list of integers or the things you wish to multipy together
# outputs:    the product of the list
def multiply(aList):
    #initiate product at 1 and use for loop to fid product of the list
    prod = 1
    #chekcs to see if aList is empty
    if len(aList) == 0:
        return 0
    #calculates product
    for num in aList:
        prod *= num
    #output product
    return prod
#end def multiply():


# createIntList() takes in a sentinel value and prompts user to make list
# input:          a sentinel value that ends list prompting when entered
# outputs:        a list that the user entered.
def createIntList(SENT_VAL):
    #initiate empty number list, first entry, and while loop for list
    numList = []
    #inputString created for the list input
    inputString = "Please enter a number, " + str(SENT_VAL) + " to stop: "
    var = int(input(inputString))
    #while the sentinel is not called
    while var != SENT_VAL:
        numList.append(var)
        var = int(input(inputString))
    #end while and output finished list
    return numList
#end def createIntList():


def main():

    print("Welcome to the Simple Math Helper")
    #get number of lists to create
    numLoops = int(input("How many lists would you like to create? "))
    #use for loop to repeate desired number of times
    #initiate values within forloop
    mathList = []
    SENTINEL = 0
    #checks to make sure that the number of loops is valid 
    if numLoops >= 0:
        for x in range(numLoops):
            #tells what list is being made
            print()
            print("You are creating list #" + str(x+1))
            #gets sentinel and calls list creator function then saves the list
            SENTINEL = int(input("What do you want the sentinel value to be? "))
            #saves list and prints it
            mathList = createIntList(SENTINEL)
            print("For the list", mathList)
            #prints out math values
            print("The summation is", summation(mathList) )
            print("The product is", multiply(mathList) )
        #end the loop
        #say goodbye
    print("Thank you for using the Simple Math Helper.")
#END MAIN

main()
