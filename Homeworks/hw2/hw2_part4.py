#File:          hw2_part4.py
#Author:        Brendan Cain
#Date:          9/21/16
#Section:       22
#E-mail:        bcain1@umbc.edu
#Description:   This program asks the user for some personal info and then
#               replaces it in a comical sort of way.
#Collaboration: Collaboration was not allowed on this assignment

def main():

    yourName = str(input("What is your name? "))
    friendName = str(input("What is your friend's name? "))
    dogName = str(input("What is your dog's name? "))
    #Gets information from user and stores every answer as a string

    print("Hello, my name is", yourName)
    print("My best friend is", dogName)
    print("I also like", friendName, "I guess.")

main()
