# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 13:55:20 2018

@author: shubham
"""

for _ in range(int(input())):
    x = int(input())
    i = 1
    count = 1
    while i <=x:
        t = i
        i+=count+1
        count+=1
    if i!=x:
        m = min(count-1+x-t, count+i-x)
        print(m)
    else:
        print(count)