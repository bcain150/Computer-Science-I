#File:          hw2_part2.py
#Author:        Brendan Cain
#Date:          9/21/16
#Section:       22
#E-mail:        bcain1@umbc.edu
#Description:   This program takes a give price and then extracts the dollars
#               from the cents and displays the amount of each as integers.
#Collaboration: Collaboration was not allowed on this assignment.

ONE_CENT = 0.01

def main():
    
    price = float(input("What is the price?: "))
    #The user inputs the price and it is saved under the float price.
    
    dollars = int(price)
    #gets the amount of dollars from price through casting & truncation.

    centsFloat = price - dollars
    cents = int(centsFloat / ONE_CENT)
    #Changes cents from a float to an int (a number less than 100)

    print("The number of dollars is: ", dollars)
    print("The number of cents is: ", cents)
    #Outputs results

main()
