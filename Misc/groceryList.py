def main():
    gList = []
    print("--Grocery List--")

    #User enters the list
    item = input("Enter an item to add to the list or 'STOP' to stop: ")
    while item != 'STOP' :
        gList.append(item)
        item = input("Enter another item or 'STOP': ")
    #END WHILE

    #Now the List is repeated back.
    print("Here is your grocery list...")
    index = 0
    while index < len(gList) :
        print("Item number", index+1, ": ", gList[index])
        index += 1
    #END WHILE
#END def main():

main()
