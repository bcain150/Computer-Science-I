# File:    semester.py
# Started: by Dr. Gibson
# Author:  Brendan Cain
# Date:    10/5/16
# Section: 22
# E-mail:  bcain1@umbc.edu 
# Description:
#   This file contains python code that asks the user for their
#   courses, then goes through the list and asks them for their
#   raw grade for each course, removes the course from the list, 
#   and calculates and prints their average grade for the semester.

def main():

    # constant for the sentinel value, and an empty list to start
    C_SENT = "NONE"
    courseList = []

    # populate the course list
    course = input("What course did you take? ('NONE' to stop): ")

    #### YOU NEED TO PUT A WHILE LOOP HERE
    while course != C_SENT :
        # save the course and ask for another
        courseList.append(course)
        course = input("What course did you take? ('NONE' to stop): ")
    #END WHILE
    # create variables to help calculate the student's average
    total = 0
    string = ""
    numClass = len(courseList)
    # go through the course list; continue while the list is not empty
    while len(courseList) != 0 :
        string = "What raw grade did you get in " + str(courseList[0]) + "? "
        # ask about their grade for each course and save it to the total
        total += input(string)
        # remove() the course from the list
        courseList.remove(courseList[0])
    #END WHILE
    # calculate their average raw grade
    avg = total/numClass
    # print out their average raw grade
    print("In the", numClass, "courses you took, you recieved a", avg, "as your raw grade.")

main()
