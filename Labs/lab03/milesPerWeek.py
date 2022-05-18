#File:          milesPerWeek.py
#Author:        Brendan Cain
#Date:          9/21/16
#Section:       22
#E-mail:        bcain1@umbc.edu
#Description:   This program calculates the total distance traveled during a
#               commute per week.
#Collaboration: During this lab collaboration between students is allowed,
#               althought I understand I still must understand the material
#               and complete the assignment myself.

CAR_SPEED = 57
#we assume that the car always goes 57mph

def main():

    milesOneWay = int(input("How many miles do you drive each way to work?: "))
    daysPerWeek = int(input("How many days do you drive to work each week?: "))
    #The previous two lines save the inputs to the the questions in quotes

    totalMiles = milesOneWay * 2  * daysPerWeek
    #Calculates total miles per week
    print("You drive ", totalMiles, " miles per week.")
    #Outputs total
    
    timeDriving = totalMiles / CAR_SPEED
    #Calculates driving time per week
    print("At ", CAR_SPEED, " mph, you spend ", timeDriving, " hours commuting in the car each week.")
    #Outputs the driving time and the constant speed for user

main()
