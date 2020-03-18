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

def combine_with_list(list_obj,list2_obj):
    print("doing combine lists ")

def combine_with_set(list_obj,set_obj):
    print("doing combine set with list ")

    


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
    elif decisionvalue == "3":
        print("Starting Problem 3")
    elif decisionvalue == "4":
        print("Ending Program")
    else:
        print("Incorrect Input")