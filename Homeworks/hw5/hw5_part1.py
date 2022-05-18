# File:          hw5_part1.py
# Author:        Brendan Cain
# Date:          10-6-16
# Section:       22
# E-mail:        bcain1@umbc.edu
# Description:   creates a modulus table using a for loop
# Collaboration: I did not collaborate with anyone on this assignment.

def main():
    #gets mod and table length from user and stores as an int
    mod = int(input("Please enter the number you would like to mod by: "))
    table = int(input("Please enter how high you would like to go: "))
    num = 0 #initializes num
    #for loop that creates the table.
    for i in range(table+1):
        num = i % mod
        print(i, "%", mod, "=", num)
    #END for loop
#END def main():

main()
