#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 20:58:07 2018

@author: shubham
"""

for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    c =[]
    if s[int(n/2)]==7:
        for i in range(int(n/2)+1):
            if s[i]==s[n-i-1]:
                c.append(1)
            else:
                c.append(2)
        if c.count(1) == len(c):
            print('yes')
        else:
            print('no')
    else:
        print('no')