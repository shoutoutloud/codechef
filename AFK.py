# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 12:42:06 2018

@author: shubham
"""

for _ in range(int(input())):
    a, b, c = map(int, input().strip().split())
    if b-a == c-b:
        print('0')
    else:
        if (a+c)%2 ==1:
            
            t = (a+c)//2
            print(min(abs(t+1-b),abs(t-b))+1)
                
        else:
            t = float(a+c)//2
            print(int(abs(t-b))) 