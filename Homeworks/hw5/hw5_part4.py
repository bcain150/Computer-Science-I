# File:          hw5_part4.py
# Author:        Brendan Cain
# Date:          10-10-16
# Section:       22
# E-mail:        bcain1@umbc.edu
# Description:   takes in a long string and a short string and finds slices
#                of the short string in the long string.
# Collaboration: I did not collaborate with anyone on this assignment.

def main():
    #take in strings
    strLng = str(input("First (longer) string: "))
    strShrt = str(input("Second (shorter) string: "))
    #use len funct to store length of strings
    lenLng = len(strLng)
    lenShrt = len(strShrt)
    #for loop to find slices
    wrd = ""
    wrdTest = strShrt.lower()
    for i in range(lenLng):
        wrd = strLng[i:i+lenShrt]#takes out a splice that's len of strShort
        wrd = wrd.lower()
        #checks to see if splice equals shorter string
        if wrd == wrdTest:
            print("At index", i, "found a slice of", strShrt)
        #Else do nothing
    #END FOR LOOP
#END def main():
main()
