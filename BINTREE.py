# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 20:18:41 2018

@author: shubham
"""

for _ in range(int(input())):
    a, b = map(int, input().split())
    t, u = a, b
    while abs(t-u) != 0:
        if t>u:
            t//=2
        else:
            u//=2
    count=0
    while a!=t:
        a//=2
        count += 1
    while b!=t:
        b//=2
        count+=1
    print(count)