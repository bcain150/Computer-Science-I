# File: games.py
# Author: Brendan Cain
# Date: 10/19/16
# Section: 22
# E-mail: bcain1@umbc.edu
# Description: a short program to help the user and their friends decide what 
# game to play. 
# Collaboration: During lab, collaboration between
# students is allowed, although I understand I still
# must understand the material and complete the
# assignment myself.

def main():
    #initiate game list
    games = ["Twister", "Dodgeball", "Capture the Flag", "Hide and Seek", 
"Croquet", "Ring Toss", "Ping Pong"]
    #print out game inventory
    for i in range(len(games)):
        print(i+1, "-", games[i])
    #prepare a sentinel for the while loop used to cast votes (constant)
    SENT = 0
    #initialize vote with first input and a vote list that corresponds to games
    votesList = [0]*len(games)
    vote = int(input("What game would you like to play? (0 to quit): "))
    while vote != SENT :
        #check to see if input is valid
        if vote > 0 and vote < 8 :
            votesList[vote-1] += 1
        #adds vote to proper tally and if it's invalid do nothing
        #gets another vote
        vote = int(input("What game would you like to play? (0 to quit): "))
    #for loop used for displaying vote results
    for i in range(len(games)):
        print(games[i], "has", votesList[i], "vote(s).")
    #END main
main()
