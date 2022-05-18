# File:          hw3_part4.py
# Author:        Brendan Cain
# Date:          9/28/16
# Section:       22
# E-mail:        bcain1@umbc.edu
# Description:   Day of the week calculator
# Collaboration: I did not collaborate with anyone on this assignment.

def main():
    #gets day of month from user
    monthDay = int(input("Enter the day of the month: "))
    #checks to make sure the day is valid.
    if monthDay < 1 or monthDay > 30 :
        print("The date", monthDay, "is an invalid day.")
    #else continues the program
    else :
        #uses mod to determind day in week
        modDay = monthDay % 7
        #Determines day of week.
        if modDay == 0 :
            print("Today is Saturday!")
        elif modDay == 1 :
            print("Today is Sunday!")
        elif modDay == 2 :
            print("Today is Monday!")
        elif modDay == 3 :
            print("Today is Tuesday!")
        elif modDay == 4 :
            print("Today is Wednesday!")
        elif modDay == 5 :
            print("Today is Thursday!")
        else :
            print("Today is Friday!")
        #END IF, ELIF, Else statements
    #END ELSE
#END def main():

main()
