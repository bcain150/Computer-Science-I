# File:    lab9.py
# Started: by Brendan Waters and Dr. Gibson
# Author:  Brendan Cain
# Date:    11-2-16
# Section: 22
# E-mail:  bcain1@umbc.edu 
# Description:
#   This file contains python code that is broken and needs
#   to be debugged.

# getNum() Get a number between 1 and 100 from the user
# Input:   None
# Output:  Integer between 1 and 100 (inclusive)

def getNum():
    msg = "Enter an integer between 1 and 100 (inclusive): "
    num = int(input(msg))
    while num < 1 or num > 100:
        print("Invalid choice!")
        num = int(input(msg))
    return num
        
# dupesByTwo() Loops through a  list to see if there are any 
#              duplicate entries separated by one other entry
# Input:       List of integers
# Output:      String (message of result)

def dupesByTwo(nums):
    resultMsg = "No dupes by two"
    for i in range(len(nums)-2):
        if nums[i] == nums[i+2]:
            resultMsg = "Found a dupe by two: " + str(nums[i])
    return resultMsg

# numsEquiv() Compare two numbers for equivalence
# Input:      Two numbers (integer or float)
# Output:     String (message of result)

def numsEquiv(num1, num2):
    resultMsg = ""

    if num1 == num2:
        resultMsg = "They match!"
    else:
        resultMsg = "No match."
    
    return resultMsg

def main():
    # TEST ONE FUNCTION AT A TIME, AND MAKE SURE IT WORKS
    # BEFORE UNCOMMENTING THE NEXT ONE

    # get a number from the user
    num1 = getNum()
    # check for duplicates separated by two, and print out the answer
    numbers = [1, 0, 4, 4, 3, 2, 6, 2, 7, 9]
    print("The result of the dupes by two test:")
    print(dupesByTwo(numbers))
    # check to see if the number from the user is the same as the last
    # number in the list of numbers from before, and print out the answer
    result = numsEquiv(num1, numbers[len(numbers)-1])
    print("The result of the equivalence test:", result)

main()
