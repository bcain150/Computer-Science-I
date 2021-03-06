# File:          hw5_part3.py
# Author:        Brendan Cain
# Date:          10-6-16
# Section:       22
# E-mail:        bcain1@umbc.edu
# Description:   print a count down from 101 to 1 with special statements
#                at multiples of 5,6 and both.
# Collaboration: I did not collaborate with anyone on this assignment.

def main():
    MAX = 101
    MIN = 1
    #use a for loop to count down
    for i in range(MAX,MIN-1,-1):
        #use if statement to determine what to print
        if i%5 == 0 and i%6 == 0:
            print("Thirty days hath September.")
        elif i%5 == 0:
            print("Where do you see yourself in five years")
        elif i%6 == 0:
            print("I'll believe six impossible things before breakfast.")
        else:
            print(i)
    #END for loop
#END main
main()
