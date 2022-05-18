# File:          hw4_part2.py
# Author:        Brendan Cain
# Date:          10/3/16
# Section:       22
# E-mail:        bcain1@umbc.edu
# Description:   Do modulus without using the mod operator "%"
# Collaboration: Collaboration was not allowed on this assignment.

def main():

    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))
    #Gets numbers from user

    intQuo = num1//num2 #does int division to get the quotient truncated.
    mod = num1-(num2*intQuo)#finds remainder and completes mod calculation.
    #outprints for user
    print(num1, "%", num2, "=", mod)
#END def main():

main()
