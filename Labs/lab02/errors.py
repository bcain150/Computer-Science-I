# File:          errors.py
# Written by:    Sue Evans
# Date:          2/10/11
# Section:       All
# UMBC Email:    bogar@cs.umbc.edu
# Description:   This program contains some buggy code that needs to be fixed.
# Collaboration: During lab, collaboration between students is allowed, 
#                although I still must understand the material and 
#                complete the assignment myself.
# Fixed by:      Brendan Cain
# Date fixed:    9/14/16

def main():
    
    print("This program finds the average of two integers.")

    num1 = int(input("Enter the first number please:  "))
    num2 = int(input("Enter the second number please: "))
    average = (num1 + num2)/2

    print("The average of the two numbers is ", average)

main()

