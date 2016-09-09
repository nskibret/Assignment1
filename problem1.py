# -*- coding: utf-8 -*-
"""
Created on Sat Sep 03 10:46:14 2016

@author: nskibret
"""
#functions defined here
def acceptList():#a list is constructed from user input
    try:
        r = int(raw_input("How many intgers in the new list? "))
    except ValueError:
        print "You did not enter integer value: default value 2"
        r = 2
    result = []
    while r>0:
        result.append(int(raw_input("Next element: ")))
        r=r-1
    return result

def findClosestElement(L,x):#given an integer value find the closest to it list
    res = []
    for i in L:
        res.append(abs(i-x))
    return res.index(min(res))
        
def removeElements(L):#Remove all elements from list L that are less than m
     m = int(raw_input("Provide an integer: "))
     result = []
     for x in L:
         if x>=m:
             result.append(x)
     return result
        
#main program begins here         
L = acceptList()

while True:
    print "\n\
    0: Exit\n\
    1: Provide a new working list\n\
    2: Output the working list\n\
    3: Find the element in the list that is closest to the value you provide\n\
    4: Sort the list\n\
    5: Add an integer you provide to each element in the list\n\
    6: Extend the working list with the list you provide\n\
    7: Remove all elements in the list less than an integer you provide"
    try:
        val = int(raw_input())
    except ValueError:
        print("Input must be integer: Exiting...")
        break
    
    if val == 0:
        print("{:<20}{:d}".format("Your selection:", val))
        break
    elif val==1:
        print("{:<20}{:d}".format("Your selection:", val))
        L = acceptList()
    elif val==2:
        print("{:<20}{:d}".format("Your selection:", val))
        print L
    elif val==3:
        print("{:<20}{:d}".format("Your selection:", val))
        x = int(raw_input("Provide an integer: "))
        CE = L[findClosestElement(L,x)]
        print("{:<20s}{:d}".format("The closest one: ", CE))
    elif val==4:
        print("{:<20}{:d}".format("Your selection:", val))
        L.sort()
    elif val==5:
        print("{:<20}{:d}".format("Your selection:", val))
        y = int(raw_input("Provide an integer: "))
        L = [y+x for x in L]
    elif val==6:
        print("{:<20}{:d}".format("Your selection:", val))
        L.extend(acceptList())
    elif val==7:
        print("{:<20}{:d}".format("Your selection:", val))
        L = removeElements(L)
    else:
        print "Invalid Input: "
        break
        
        