# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 22:02:39 2016

@author: nskibret
"""

#functions definition goes here
def createTable(n):
    result = {}
    while n>0:
        name = raw_input("Name: ")
        account = float(raw_input("Initial balance: "))
        result[name]=account
        n=n-1
    return result

def displayCurrentBalances(D,keys):
    for x in keys:
        print("{0:>10s}".format(x)),
    print "\n",

    for y in keys:
        if D[y]<0:
            out = "-$"+"{:.2f}".format(-D[y])
        else:
            out = "$"+"{:.2f}".format(D[y])
        print(out.rjust(10)),
    print "\n",


def displayTransactionRecord(L,keys):#display transactions done 
    for i,T in enumerate(L):
        print("{:>5d}".format(i+1)),
        for x in keys:
            if T[x]<0:
                out = "-$"+"{:.2f}".format(-T[x])
            else:
                out = "$"+"{:.2f}".format(T[x])
            print(out.rjust(10)),
        print "\n",
    
    
    
#Main program begins here
L_table = []
N_account = int(raw_input("Number of accounts: "))
table = createTable(N_account)
keys = table.keys()
values = table.values()
old_table = {}

while True:
    for x in keys:
        print "\nProcessing ",x
        print "Transaction type:"
        print "\
        0: Nothing\n\
        1: Deposit\n\
        2: Withdrawal"
        value = int(raw_input(": "))
        if value == 0:
            old_table[x]=0
        elif value==1:
            y = float(raw_input("Amount: "))
            table[x] = table[x]+y
            old_table[x]=y
        elif value==2:
            h = float(raw_input("Amount: "))
            table[x] = table[x]-h
            old_table[x]=-h
        else:
            print "Invalid Input: "
            
    L_table.append(old_table.copy())       
    print("{:<}".format("Current Balances"))
    displayCurrentBalances(table,keys) #display current balance shit for all customers
    print "\n",
    repeat = raw_input("0 to exit, any other key to continue: ") #user wants to process or exit
    if repeat == '0':
        break          #break out of the while loop
    

print("{:<20s}".format("\nRecord of Transactions"))
print("{0:>5s}".format("Round")),
for x in keys:
    print("{0:>10s}".format(x)),
hh = "\n"+"-"*(len(keys))*11+"-"*5
print hh
displayTransactionRecord(L_table,keys)
