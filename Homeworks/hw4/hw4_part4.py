# File:          hw4_part3.py
# Author:        Brendan Cain
# Date:          10/4/16
# Section:       22
# E-mail:        bcain1@umbc.edu
# Description:   Code that simulates the up and down movement
#                of a hailstone in a storm.
# Collaboration: Collaboration was not allowed on this assignment.

def main():

    hail = int(input("Please enter the starting height for the hailstone: "))
    #loops while the height is greater than 1
    while hail > 1:
        #outputs current height of the hail.
        print("Hail is currently at height", hail)
        #Checks to see if height is even and then manipulates it respectively
        if hail%2 == 0:
            hail = hail/2
        else:
            hail = (hail*3) + 1  
    #End While
    print("Hail stopped at height", hail)
#END def main():

main()
