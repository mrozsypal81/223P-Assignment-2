#Assignment 2 by Michael Rozsypal
#Problem 1 Python Lambda Function


decisionvalue = None


while decisionvalue != 4 :
    
    print('===========================================================================================')
    print('')
    print("Which problem would you like to choose")
    print('')
    print("Problem 1 enter 1")
    print('')
    print("Problem 2 enter 2")
    print('')
    print("Problem 3 enter 3")
    print('')
    print("To quit enter 4")
    print('')
    decisionvalue = input("Please enter your input now ")
    print('===========================================================================================')
    
    if decisionvalue == "1":
        print("Starting Problem 1")
    elif decisionvalue == "2":
        print("Starting Problem 2")
    elif decisionvalue == "3":
        print("Starting Problem 3")
    elif decisionvalue == "4":
        print("Ending Program")
    else:
        print("Incorrect Input")