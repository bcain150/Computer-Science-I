# File: proj1.py
# Author: BrendanCain
# Date: 11-7-16
# Section: 22
# E-mail: bcain1@umbc.edu
# Description: allows two players to play connect4
# Collaboration: Collaboration was not allowed on this assig

#printBoard() prints the current contents of the connect 4 board
#input: a 2D list
#output: nothing

def printBoard(con4List):
    print()
    # use a double for loop to print each place on the board
    # use a range function with a negative step to move backwards
    # in the list so that the bottom of the board is closest to 
    # the bottom of the screen
    for r in range(len(con4List)-1,-1,-1):
        rowStr = " " #add a blank space between every board space.
        for col in con4List[r]:
            rowStr += (col + " ")
        #prints the whole row
        print(rowStr)
    #end for loops
    print()
#end def printBoard()

# createBoard() creates a connect 4 board with dimensions greater than 5x5
# input: nothing
# output: a 2D list connect4 board

def createBoard():
    #constants
    MIN_NUM = 5
    EMPTY_SPACE = "_"

    #prompt for rows and check validity using while loop
    print("Please choose the number of rows: ")
    msg = "Please enter a number greater than or equal to "+str(MIN_NUM)+": "
    row = int(input(msg))
    while row < MIN_NUM:
        row = int(input(msg))

    #prompt for columns and check validity using a while loop
    print("Please chose the number of columns: ")
    column = int(input(msg))
    while column < MIN_NUM:
        column = int(input(msg))

    #creates the board
    boardList = []
    for r in range(row):
        col = []
        for c in range(column):
            col.append(EMPTY_SPACE)
        boardList.append(col)
    
    return boardList
#end def createBoard()

# save() saves a board to a file
# input: the 2D list board
# output: nothing

def save(con4List):
    #prompt user for a save name
    saveName = str(input("What game file would you like to save to? "))
    saveVar = open(saveName, "w")
    #opens save and makes it useable to "w" for writing
    #uses double foor loop to write to list

    for row in con4List:
        line = ""
        for i in row:
            #adds a space in between each 2D list position
            #this makes it easier to load a save bc a " " is the delimeter
            line += (i+" ")
        #writes the line to the file
        saveVar.write(line + "\n")
    #end for loops
    saveVar.close()
    print("File saved")
#end def save():

# load() loads a specific save file
# input: nothing
# output: the save 2dList board

def load():
    #prompt user for the save name that they wish to load
    saveName = str(input("What game file would you like to load from? "))
    saveVar = open(saveName, "r")
    
    #read in save and use for loop to split  
    board = saveVar.readlines()
    for i in range(len(board)):
        board[i] = board[i].split()
    # return recreated board
    saveVar.close()
    return board
#end def load()

# takeTurn() executes one player's turn and outputs the resulting board
# input: the 2D List
# output: the modified 2D List

def takeTurn(con4List):

    #gets the piece and lets the user know who's turn it is.
    piece = getTurn(con4List)    
    if piece == 'x':
        print("Player 1 what is your choice? ")
    else:
        print("Player 2 what is your choice? ")

    #gets dimensions of board
    width = len(con4List[0])
    height = len(con4List)

    #checks to make sure column is not full and the col choice is valid
    colFull = True
    while(colFull):
        colChoice = getColumn(con4List)
        #rechecks col availablity
        colFull = checkCol(con4List, colChoice)
    #end while
    
    #places the connect 4 piece at the bottom of the column
    place = 0
    while con4List[place][colChoice] != '_':
        place += 1
    #ammends the connect 4 List
    con4List[place][colChoice] = piece

    return con4List
#end def takeTurn():

#getTurn() evaluates who's turn it is to place a piece
#input: the connect 4 board (2D List)
#output: the piece of who's turn it is (in the form of a str)

def getTurn(con4List):
    #Finds who's turn it is by going through the list
    #and checking if the number of total turns is even or odd.
    turnCnt = 0
    for row in con4List:
        for i in row:
            if i == 'x' or i == 'o':
                turnCnt += 1
    #end for
    piece = ""
    #sets the piece based on whether total moves are
    #even or odd.
    if turnCnt%2 == 0:
        piece = 'x'
    else:
        piece = 'o'
    #returns the correct player's piece
    return piece

#end def getTurn():
    
#checkCol() checks to see if the col is full
#input: the connect 4 2D array, and the column chosen
#output: true or false on whether the column is empty

def checkCol(con4List, column):
    l = len(con4List)-1 #the top row index
    top = con4List[l]
    #checks to see if there is an x or an o in the top row
    if top[column] == 'x' or top[column] == 'o':
        print("Column is full.")
        return True
        #returns true if full
    else:
        return False
        #returns false if available
#end checkCol
        
# getColumn() gets the valid user inputed column and saves to a file if necessary
#input: the connect 4 2D List
#output: the column choice
    
def getColumn(con4List):

    width = len(con4List[0])
    #gets a column input from the user
    SAVE_KEY = "s"
    msg = "Please choose a column to place your piece in (1 - " + str(width) + ") or " + SAVE_KEY + " to save: "
    col = input(msg)
    #while loop that determines if the input is correct
    #minimum parameter will always be 1 because column numbers start at 1
    while col == SAVE_KEY or (int(col) < 1 or int(col) > width):
        #Saves to file
        if col == SAVE_KEY:
            save(con4List)
        # re prompt user
        col = input(msg)
    #end while
    return int(col)-1
#end getColumn()

#endGame() checks to see if someone has won connect4 and outputs the outcome of the game
#input: the connect4 board (a 2D list)
#output: boolean depending on if the game is over or not

def endGame(con4):
    #gets board dimensions
    rows = len(con4)
    cols = len(con4[0])
    #determines who just placed a piece
    #the if statement is necessary b/c getTurn returns who's turn it currently is,
    #not who just took their turn. (this is what we want)
    p = getTurn(con4)
    if p == "x":
        p = "o"
    else:
        p = "x"
    #starts checks and initializes winner
    winner = ""
    
    #STALEMATE CHECK
    area = rows*cols
    #gets total turns
    turnCnt = 0
    for row in con4:
        for i in row:
            if i == 'x' or i == 'o':
                turnCnt += 1
    #if all the spaces are filled the winner = "n" for "none"
    if turnCnt == area:
        winner = "n"

    #VERTICAL CHECK
    if winner == "":
        #only checks if there is still no winner
        for r in range(rows-3):
            for c in range(cols):
                if p==con4[r][c] and p==con4[r+1][c] and p==con4[r+2][c] and p==con4[r+3][c]:
                    winner = p

    #HORIZONTAL CHECK
    if winner == "":
        #only checks if there is still no winner
        for r in range(rows):
            for c in range(cols-3):
                if p==con4[r][c] and p==con4[r][c+1] and p==con4[r][c+2] and p==con4[r][c+3]:
                    winner = p
    
    #RIGHT-LEANING DIAGONAL CHECK
    if winner == "":
        for r in range(rows-3):
            for c in range(3,cols):
                if p==con4[r][c-3] and p==con4[r+1][c-2] and p==con4[r+2][c-1] and p==con4[r+3][c]:
                    winner = p
            
    #LEFT-LEANING DIAGONAL CHECK
    if winner == "":
        for r in range(3,rows):
            for c in range(cols-3):
                if p==con4[r][c] and p==con4[r-1][c+1] and p==con4[r-2][c+2] and p==con4[r-3][c+3]:
                    winner = p
    
    #END CHECKS and print
   
    if winner == "x":
        printBoard(con4)
        print("Player 1 wins!")
        return False
    elif winner == "o":
        printBoard(con4)
        print("Player 2 wins!")
        return False
    elif winner == "n":
        printBoard(con4)
        print("There is a draw!")
        return False
    else:
        return True

def main():
    #makes the connect four board
    connectFour = []
    #Prints opening statements
    print("Welcome to Connect Four")
    print("This game is for two players")
    
    #this loops until the user wishes to stop playing.
    play = "y"
    while play == "y":
        
        #loads a game if the user wishes
        q = "Would you like to load a game (y/n)? "
        loadQ = input(q)
        #while loop checks input
        while loadQ != 'y' and loadQ != 'n':
            loadQ = input(q)
        #executes the loading of a game or creates the game
        if loadQ == 'y':
            connectFour = load()
        else:
            connectFour = createBoard()

        #Now the board is created so the game can begin
        stillPlaying = True
        while stillPlaying:
            printBoard(connectFour)
            connectFour = takeTurn(connectFour)
            #checks for a winner
            stillPlaying = endGame(connectFour)

        #asks the user if they wish to play again.
        q = "Would you like to play again (y/n): "
        play = input(q)
        #validates input
        while play != 'y' and play != 'n':
            play = input(q)
        #if the user wishes to play again or play == 'y' then the outer loop will loop agian
        #otherwise the game ends and the program exits
    print()
    print("Thanks for playing")
#END def main():

main()

