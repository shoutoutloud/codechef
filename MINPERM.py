#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 21:06:04 2018

@author: shubham
"""

for _ in range(int(input())):
    n = int(input())
    s = [] 
    for i in range(1,n+1):
        s.append(i)
    for j in range(len(s)):
        if s[j] == j+1:
            if j<n-1:
                temp = s[j]
                s[j] = s[j+1]
                s[j+1] = temp
            else:
                temp = s[j]
                s[j] = s[j-1]
                s[j-1] = temp
    for k in range(n):
        print(s[k], end = " ") 