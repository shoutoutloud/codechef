# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 13:00:28 2018

@author: shubham
"""

for _ in range(int(input())):
    n, d = input().split()
    s = []
    for i in range(int(n)):
        s.append(input())
    cDee = 0
    cDum = 0
    for i in s:
        if i[0] == '1':
            cDum+=i.count('1')
        else:
            cDee += i.count('0')
    if cDee==cDum:
        if d=='Dee':
            print("Dum")
        else:
            print("Dee")
    elif cDum>cDee:
        print("Dum")
    else:
        print("Dee") 