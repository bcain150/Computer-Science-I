PASS_WRD = "Doggo"
MAC_TRIES = 3

def main():
    guess = str(input("Guess the password: "))
    guessCnt = 1
    while guess != PASS_WRD and guessCnt < MAX_TRIES :
        guess = str(input("Sorry guess again: "))
        guessCnt += 1
    #END while

    if guess == PASS_WRD :
        print("YOU GOT IT RIGHT BOI, in ", guessCnt, " tries!")
    else :
        print("Sorry you are some cut and couldn't guess it right.")

#END def main():
main()

