#Assignment 2 by Michael Rozsypal
#Problem 1 Python Lambda Function

import itertools
import functools

#variables for usesinput and tables for entries
userinput = None
#This is the main table that holds all entries There are initial values here for testing purposes
#The program may error if the table is empty
Maintable = [{'First_Name':'Mike1','Last_Name':'Rozy1','CWID':'abcd','ClassID':'class1'},
            {'First_Name':'Mike2','Last_Name':'Rozy2','CWID':'efg','ClassID':'class1'},
            {'First_Name':'Mike3','Last_Name':'Rozy3','CWID':'hijk','ClassID':'class2'},
            {'First_Name':'Mike4','Last_Name':'Rozy4','CWID':'lmn','ClassID':'class1'},
            {'First_Name':'Mike5','Last_Name':'Rozy5','CWID':'opq','ClassID':'class3'}]

#This table holds all correlations between classID and CWID
ClassCWIDtable = {'class1':{'abcd','efg','lmn'},'class2':{'hijk'},'class3':{'opq'}}
#value that lets the user navigate the UI
decisionvalue = None
#This Function Takes newly created student entries and adds them to the appropriate place on the ClassCWIDtable
def ClassCWID(studententry):
    temp = None
    for key in ClassCWIDtable:
        print(key)
        if key == studententry['ClassID']:
            temp = key
    if temp != None:
        ClassCWIDtable[temp].add(studententry['CWID'])
        return

    ClassCWIDtable.update({studententry['ClassID']:{studententry['CWID']}})



#This function creates new student entries on the maintable
def addentryfunc():
    fileopen = input("Please input the file name and extension that you wish to open now ")
    with open(fileopen,'r') as f:
        for line in f:
            x = 0
            newstudent = {}
            for word in line.split():
                if x == 0:
                    newstudent.update({'CWID':word})
                    x += 1
                if x == 1:
                    newstudent.update({'First_Name':word})
                    x += 1
                if x == 2:
                    newstudent.update({'Last_Name':word})
                    x += 1
                if x == 3:
                    newstudent.update({'Gender':word})
                    x += 1
                if x == 4:
                    newstudent.update({'DOB':word})
                    x += 1
                if x == 5:
                    newstudent.update({'ClassID':word})
                    x += 1
                if x == 6:
                    newstudent.update({'Grade':word})
                    x += 1
            Maintable.append(newstudent)
            ClassCWID(newstudent)

                




#This function prints out every class along with its associated students
def printentriesfunc():
    print('===========================================================================================')
    for key,value in ClassCWIDtable.copy().items():
        print('The classID is '+ key)
        for setvalue in value:
            for x in Maintable:
                if x['CWID'] == setvalue and x['ClassID'] == key:
                    print('CWID: '+ setvalue+' First Name '+x['First_Name']+' Last Name '+x['Last_Name'])
    print('===========================================================================================')


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
            #print(type(i).__name__)
            if type(i).__name__ == "str":
                if i.isdigit() and float(i) >= 4:
                   # print("adding a number to l1")
                    newlist1.append(i)
                elif ((i.startswith('-') and i[1:].isdigit()) == False) and (i.isdigit() == False):
                    #print("adding a string split list to l1")
                    temp = i
                    temp = (temp.split(','))
                    for x in temp:
                        newlist1.append(x)
                #elif ((i.startswith('-') and i[1:].isdigit()) == False) and (i.isdigit() == False):
                    #print("adding a string to l1")
                    #newlist1.append(i)
            #if type(i).__name__ == "int":
                if i >= 4:
                    newlist1.append(i)
        for i in obj2:
            #print(type(i).__name__)
            if type(i).__name__ == "str":
                if i.isdigit() and float(i) >= 4:
                    #print("adding a number to l2")
                    newlist2.append(i)
                elif ((i.startswith('-') and i[1:].isdigit()) == False) and (i.isdigit() == False):
                    #print("adding a string split list to l2")
                    temp = i
                    temp = (temp.split(','))
                    for x in temp:
                        newlist2.append(x)
                #elif ((i.startswith('-') and i[1:].isdigit()) == False) and (i.isdigit() == False):
                    #print("adding a string to l2")
                    #newlist2.append(i)
            if type(i).__name__ == "int":
                if i >= 4:
                    newlist2.append(i)
            
        returned_value = func(newlist1,newlist2)

        return returned_value

    return inner

@moddec
def combine_with_list(list_obj,list2_obj):
    #print("doing combine lists ")

    return list_obj + list2_obj
@moddec
def combine_with_set(list_obj,set_obj):
    #print("doing combine set with list ")
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
        decisionvalue = "0"
        while decisionvalue != "1" and decisionvalue != "2" and decisionvalue != "3":
            print('===========================================================================================')
            print("If you would like to combine two lists press 1 ")
            print("If you would like to combine a list and a set press 2 ")
            print("If you would like to cancel press 3 ")
            print('===========================================================================================')

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
        addentryfunc()
        printentriesfunc()
    elif decisionvalue == "4":
        print("Ending Program")
    else:
        print("Incorrect Input")