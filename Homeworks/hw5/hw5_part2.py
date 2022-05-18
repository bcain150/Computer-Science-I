# File:          hw5_part2.py
# Author:        Brendan Cain
# Date:          10-6-16
# Section:       22
# E-mail:        bcain1@umbc.edu
# Description:   draws a box using symbols
# Collaboration: I did not collaborate with anyone on this assignment.

def main():
    #get dimensions and characters
    width = int(input("Enter the width of the box: "))
    height = int(input("Enter the height of the box: "))
    outer = str(input("Enter a character for the box outline: "))
    inner = str(input("Enter a character for the box fill: "))
    #a for loop draws the box line by line
    for h in range(height):
        #determines when to print outline or fill character
        if h == 0 or h == height-1 :
            print(outer*width)
        else:
           print(outer + inner*(width-2) + outer)
    #end for loop
#end def main():
main()
