# File:          hw3_part2.py
# Author:        Brendan Cain
# Date:          9/26/16
# Section:       22
# E-mail:        bcain1@umbc.edu
# Description:   This program asks questions about the user's dog to guess
#                it's breed.
# Collaboration: I did not collaborate with anyone on this assignment.

def main():
    YES = 'yes'
    NO = 'no'
    print("---Dog breed guesser---")
    print("Answer only 'yes' or 'no' to the following questions.")
    
    #Determines breed by asking at lease 2 questions but no more than 3
    if str(input("Is the dog a big dog?: ")) == YES :
        if str(input("Does the dog have a fluffy coat?: ")) == YES :
            dog = 'Samoyed.'
        elif str(input("Do your dog's ears stick up?: ")) == YES :
            dog = 'German Sheperd.'
        else :
            dog = 'Borzoi.'
    elif str(input("Does your dog have a curly tail?: ")) == YES :
        dog = 'Shiba Inu.'
    else :
        dog = 'Corgi.'
    #END if, elif, else statements
    
    print("Your dog is a", dog)
    #outputs dog breed.

#END main
main()
