#File:          hw2_part1.py
#Author:        Brendan Cain
#Date:          9/21/16
#Section:       22
#E-mail:        bcain1@umbc.edu
#Description:   This program calculates the total cost to buy and ship a large 
#               order of books from an online bookstore.
#Collaboration: Collaboration was not allowed on this assignment.

TAX = 0.06
SHIPPING = 6.95
#These variables are constants. TAX is the tax percentage and SHIPPING 
#is the cost of shipping per book.

def main():

    bookPrice = float(input("What is the price of the book?: "))
    numCopies = int(input("How many copies do you want?: "))
    #These variables store the users inputs of the price and number of books

    subTotal = bookPrice * numCopies
    taxCost = subTotal * TAX
    shipCost = numCopies * SHIPPING
    total = subTotal + taxCost + shipCost
    #The 4 lines above compute the sub-total, the cost of taxes, and the cost
    #of shipping and then adds all of them together

    print("The total cost is $", total)
    #Outputs the total cost of order to user.

main()
