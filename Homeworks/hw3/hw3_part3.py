# File:          hw3_part3.py
# Author:        Brendan Cain
# Date:          9/28/16
# Section:       22
# E-mail:        bcain1@umbc.edu
# Description:   takes the temperature input and outputs water's state of
#                matter at that temperature. (handles Celcius and Kelvin).
# Collaboration: I did not collaborate with anyone on this assignment.

def main():
    FREEZE = 0
    BOIL = 100
    CONVERT = 273.15
    temp = float(input("Please enter the temperature: "))
    print("Please enter the units...")
    units = str(input("Either 'K' for Kelvin or 'C' for Celcius: "))
    #Collect temperature and units of measure.
    
    #Converts to celcius if temp is in Kelvin
    if units == 'K' :
        tempCel = temp - CONVERT
    else :
        tempCel = temp

    if tempCel <= FREEZE :
        print("At this temperature, water is a (frozen) solid.")
    elif tempCel < BOIL :
        print("At this temperature, water is a liquid.")
    else :
        print("At this temperature, water is a gas.")
    #The above statements determine the state of matter of water at that temp
    #and then communicates it to the user.
    #END if, elif, else statements
#END def main():

main()
