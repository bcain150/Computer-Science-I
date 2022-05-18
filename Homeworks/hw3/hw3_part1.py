# File:          hw3_part1.py
# Author:        Brendan Cain
# Date:          9/26/16
# Section:       22
# E-mail:        bcain1@umbc.edu
# Description:   user inputs a foating point number and the output is whether
#                number is positive, negative or, zero.
# Collaboration: I did not collaborate with anyone on this assignment.

def main():
    num = float(input("Please enter a floating point number: "))
    
    if num < 0 :
        print("The number ", num, " is negative.")
    
    elif num > 0 :
        print("The number ", num, " is positive.")
    
    else :
        print("The number ", num, " is equal to zero.")

#End of Def Main

main()
