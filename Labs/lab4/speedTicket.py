# File Name:     speedTicket.py 
# Author:        Brendan Cain 
# Date:          09/28/16 
# Section:       22 
# E-mail:        bcain1@umbc.edu 
# Description:   a program to help a police officer calculate the appropriate 
#                fine for driving over the speed limit.  
# Collaboration: During lab, collaboration between students is allowed, 
#                although I understand I still must understand the material 
#                and complete the assignment myself. 

def main():
    
    #Officer enters information:
    spdLimit = int(input("Enter the speed limit in MPH: "))
    driveSpd = int(input("Enter the driving speed in MPH: "))

    #Calculates how much the driver was speeding by and then outputs to user
    speedDiff = driveSpd - spdLimit
    print("You were over the speed limit by", speedDiff, "MPH.")

    if speedDiff < 10 :
        print("You receive no ticket... this time.")
        #output when the driver is less than 10MPH over the speed limit
    elif speedDiff <= 25 :
        print("You receive a ticket for a $75 fine.")
        #output when the driver is 10 - 25 mph (inclusive!) over.
    elif speedDiff < 30 :
        print("You receive a ticket for a $150 fine.")
        #output when driver is 25 - 30 mph over the speed limit (exlusive!)
    else:
        print("You get a ticket for a $500 fine, and mandatory court date.")
        #output when the driver is 30mph or more over the speed limit
    #End speeding penalty determination.

#END def main():
main()
