# File: hw8.py
# Author: Brendan Cain
# Date: 11/21/16
# Section: 22
# E-mail: bcain1@umbc.edu
# Description: a simulation of the “Sorting Hat” from the Harry Potter books
# Collaboration: I did not collaborate with anyone on this assignment.

import random

#printOneHouse() prints the name of the house and the people in it if the house exists
#input: the house name as a string, and the dictionary of the hogwarts houses and their members
#output: none

def printOneHouse(houseName, hogD):
	#checks to make sure that the house name is in the directory
	if houseName in list(hogD.keys()):
		#then prints the name of the house and it's members
		print("The members of the House of", houseName, "are:")
		#a for loop is used to print the members
		for p in hogD[houseName]:
			print("\t", p)
	#if the house doesn't exist, then say so.
	else:
		print("There is no house by the name of", houseName)
#END def printOneHouse

#printAllHouses() prints every house and it's members in the dictionary.
#input: the hogwarts dictionary
#output: none

def printAllHouses(hogD):
	#calls printOneHouse for every house in the directory
	for h in list(hogD.keys()):
		printOneHouse(h, hogD)
#END def printAllHouses()

#houseSort() asks the user for their house preference and then sorts them into a random house.
#input: the original hogwarts dictionary
#output: the appended directory with the student placed in a house

def houseSort(hogD):
	#get's persons name and their prefered house.
	name = input("What is the person's name? ")
	prefHouse = input("What house do they prefer? ")
	#gets a list of all the houses in the dictionary and checks to see if the prefered house
	#is in that list
	houseList = list(hogD.keys())
	if prefHouse in houseList:
		#modifies houseList to increase chances of that house being picked (n+1)/(n*2)
		for i in range(len(houseList)):
			houseList.append(prefHouse)
	#picks a random house from the list
	house = random.choice(houseList)
	#prints out choice to user
	print(name, "was sorted into house", house)
	#updates the dictionary and returns it
	hogD[house].append(name)
	return hogD
#END def houseSort

#valNum() gets a valid number within min-max
#input: min and max
#output: the number choice

def valNum(minn, maxx):
	#create message to prompt input
	msg = "Please enter a number between "+str(minn)+" and "+str(maxx)+" (inclusive) : "
	num = int(input(msg))
	#sets up while loop if number is invalid
	while(num < minn or num > maxx):
		print("That number is invalid!")
		num = int(input(msg))
	return num
#END def valNum

#convDict() reads in the Hogwarts Directory text file and converts it to a dictionary of Lists
#input: the text file string name
#output: the dictionary

def convDict(fileName):
	#open file
	direct = open(fileName, 'r')
	#read in lines and initiates dictionary
	sortList = direct.readlines()
	hogD = {}

	for i in sortList:
		#split on a comma
		j = i.split(',')
		j[1] = j[1].strip()
		tempList = [j[1]]
		#checks to see if the house already exists.
		#if it doesn't create the key:value pair
		if j[0] not in list(hogD.keys()):
			hogD[j[0]] = tempList
		else:
			#other wise append the value at the key
			hogD[j[0]].append(j[1])
	#end for
	return hogD
#END def convDict()

def main():
	#gets file name
	file_name = input("Please enter a filename to load from: ")
	hogwarts = convDict(file_name)
	i = 0
	#main program loop
	while i != 4:
		#prints menu
		print()
		print("Please make a choice from the menu: ")
		print("1 - Print a single house")
		print("2 - Print all the houses")
		print("3 - Sort a new person into a house")
		print("4 - Exit the program")
		print()
		#calls a valid menu choice
		i = valNum(1,4)
		#executes program based on menu choice
		if i == 1:
			house = input("What house's members would you like to print? ")
			printOneHouse(house, hogwarts)

		elif i == 2:
			printAllHouses(hogwarts)

		elif i == 3:
			houseSort(hogwarts)
		#separates different menu processes
		print()
		print((("-"*5)+" ")*5)
	#END while
	print("Thank you for using the Great Houses Program")
#END def main():

main()
