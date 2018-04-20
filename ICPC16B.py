# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 12:42:53 2018

@author: shubham
"""

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    flag =0
    x = n-a.count(0)-a.count(1)-a.count(-1)
    if x>1:
        print("no")
    elif a.count(-1)>1 and a.count(1)==0:
        print("no")
    elif a.count(-1)>0 and x>0:
        print("no")
    else:
        print("yes")
         