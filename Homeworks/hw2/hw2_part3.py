#File:          hw2_part3.py
#Author:        Brendan Cain
#Date:          9/21/16
#Section:       22
#E-mail:        bcain1@umbc.edu
#Description:   This program functions like a shopping list app.
#Collaboration: Collaboration was not allowed on this assignment.

def main():

    item1 = str(input("What would you like to buy first?: "))
    print("You are buying ", item1, ".")
    amt1 = int(input("How many would you like to buy?: "))
    #Asks user what they are buying and how many of them

    item2 = str(input("What would you like to buy second?: "))
    print("You are buying ", item2, ".")
    amt2 = int(input("How many would you like to buy?: "))

    item3 = str(input("What would you like to buy third?: "))
    print("You are buying ", item3, ".")
    amt3 = int(input("How many would you like to buy?: "))
    #Repeats for 3 items

    totalAmt = amt1 + amt2 + amt3
    #Calculates total number of items that you are purchasing

    print("You are buying ", totalAmt, " items:")
    print(amt1, item1)
    print(amt2, item2)
    print(amt3, item3)
    #Outputs the Shopping list

main()
