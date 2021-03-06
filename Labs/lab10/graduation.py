# File:        graduation.py
# Author:      Brendan Cain
# Date:        11-9-16
# Section:     22
# E-mail:      bcain1@umbc.edu
# Description: simulates a graduation ceremony
# Collaboration: During lab, collaboration between students is allowed,
#                although I understand I still must understand the material
#                and complete the assignment myself.

def main():
    FILE_NAME = "roster.txt"
    #opens file for reading
    roster = open(FILE_NAME, "r")
    #makes an array of each line
    rosterList = roster.readlines()
    
    #for loop splits up the information in each line and writes it to a 2dList
    for i in range(len(rosterList)):
        #splits up strings using a semi-colon as a delimeter
        rosterList[i] = rosterList[i].split(';')
    #end for
    #now rosterList is a 2DList where the 1 d part is the List of grad info.
    roster.close()
    
    OUTPUT = "output.txt"
    grad = open(OUTPUT, "w")
    
    # the indexes of each graduates information
    fstNmI = 3
    lstNmI = 2
    gpaI = 1
    majI = 0

    #for loop to write to the graduation announcement
    for info in rosterList:
        wrtStr = info[fstNmI].strip() + " " + info[lstNmI] + " is graduating with a degree in " + info[majI] + "\n"
        grad.write(wrtStr)
    #end for
    grad.close()
    
    #checks for validictorian
    highGPA = 0
    valName = ""
    for info in rosterList:
        #compares highest gpa
        if float(info[gpaI]) > highGPA:
            highGPA = float(info[gpaI])
            valName = info[fstNmI].strip() + " " + info[lstNmI]
        #else do nothing
    #end for
    
    print(valName, "is the valadictorian with a GPA of", highGPA)
#end def main():
    
main()
