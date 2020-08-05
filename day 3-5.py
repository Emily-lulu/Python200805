# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 14:30:14 2020

@author: user
"""
def y():
    b=input('type a number')
    c=input('type a number')
    c=int(c)
    b=int(b)
    return(b,c)

a=0
while a==0:
    print('1. add')
    print('2. subtract')
    print('3. times')
    print('4. divide')
    print('5. leave')
    x=input('please pick a option')
    x = int(x)
    if x==1:
        b,c=y()
        print('the answer is',b+c)
    elif x==2:
        b,c=y()
        print('the answer is', b-c)
    elif x==3:
        b,c=y()
        print('the answer is', b*c)
    elif x==4:
        b,c=y()
        print('the answer is', b/c)
    elif x==5:
        break