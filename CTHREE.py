#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 22:07:32 2018

@author: shubham
"""
for _ in range(int(input())):
    n, a, b, c = map(int, input().split())
    s= []
    for i in range(1, a):
        if n%i == 0:
            s.append(i)
    for i in range(1, b):
        if n%i == 0 and i not in s:
            s.append(i)
    for i in range(1, c):
        if n%i == 0 and i not in s:
            s.append(i)
    count = 0
    for i in s:
        p = n//i
        for j in s:
            if p%j==0:
                if p//j <=c:
                    count+=1          
    print(count)