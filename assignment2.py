#Assignment 2 by Michael Rozsypal
#Problem 1 Python Lambda Function

import itertools
import functools


decisionvalue = None


def lambdafunc(r,n,m):

    return lambda a,x,y : (a/r)*(x**n)*(y**m)

def cal_poly_func(r,n,m):
    outputl = []
    newlam = lambdafunc(r,n,m)
    for (i,j,k) in zip(a,x,y):
        outputl.append(newlam(i,j,k))
    return outputl

def moddec(func):
    def inner(obj1,obj2):
        newlist1 = []
        newlist2 = []
        for i in obj1:
            print(type(i).__name__)
            if type(i).__name__ == "str":
                if i.isdigit() and float(i) >= 4:
                    newlist1.append(i)
                elif ((i.startswith('-') and i[1:].isdigit()) == False) and float(i) >= 4:
                    newlist1 + (i.split(','))
            if type(i).__name__ == "int":
                if i >= 4:
                    newlist1.append(i)
        for i in obj2:
            print(type(i).__name__)
            if type(i).__name__ == "str":
                if i.isdigit() and float(i) >= 4:
                    newlist2.append(i)
                elif ((i.startswith('-') and i[1:].isdigit()) == False) and float(i) >= 4:
                    newlist2 + (i.split(','))
            if type(i).__name__ == "int":
                if i >= 4:
                    newlist2.append(i)
            
        returned_value = func(newlist1,newlist2)

        return returned_value

    return inner

@moddec
def combine_with_list(list_obj,list2_obj):
    print("doing combine lists ")

    return list_obj + list2_obj
@moddec
def combine_with_set(list_obj,set_obj):
    print("doing combine set with list ")
    newlist = list(set_obj)

    return list_obj + newlist

    


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
        r,n,m = input("Enter three values with spaces inbetween for constants ").split()

        r = int(r,10)
        n = int(n,10)
        m = int(m,10)

        a = list(map(int,input("Enter values for the first list a: ").split()))
        x = list(map(int,input("Enter values for the second list x: ").split()))
        y = list(map(int,input("Enter values for the third list y: ").split()))

        outputl = cal_poly_func(r,n,m)

        outputsum = functools.reduce(lambda a,b : a + b,outputl)

        print("The sum of the lists together modified by the constants is ", outputsum)

    elif decisionvalue == "2":
        print("Starting Problem 2")
        
        while decisionvalue != 1 or decisionvalue != 2 or decisionvalue != 3:
            print("If you would like to combine two lists press 1 ")
            print("If you would like to combine a list and a set press 2 ")
            print("If you would like to cancel press 3 ")

            decisionvalue = input("Please enter input now ")
    
        if decisionvalue == "1":
            l1 = list(map(str,input("Enter values for the first list: ").split()))
            l2 = list(map(str,input("Enter values for the second list: ").split()))
            newlist = combine_with_list(l1,l2)
            print(newlist)

        elif decisionvalue == "2":
            l1 = list(map(str,input("Enter values for the list: ").split()))
            s1 = set(map(str,input("Enter values for the set: ").split()))
            newlist = combine_with_set(l1,s1)
            print(newlist)
        elif decisionvalue == "3":
            print("Cancelled going back to main menu ")

    elif decisionvalue == "3":
        print("Starting Problem 3")
    elif decisionvalue == "4":
        print("Ending Program")
    else:
        print("Incorrect Input")