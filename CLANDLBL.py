#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 00:37:03 2018

@author: shubham
"""

for _ in range(int(input())):
    n =int(input())
    m = [0]*n
    for i in range(n):
        m[i] = list(map(int, input().split()))
    flag =0
    
    if n==1:
        t = []
        t.append(1)
    elif n == 2:
        t = []
        t.append(2)
        t.append(1)
    elif n == 3:
        t = []
        t.append(3)
        t.append(2)
        t.append(1)
    else:
        t = [0]*n
        for i in range(n):
            for j in range(n):
                if m[i][j]==2:
                    t[i] = i+1
                    t[j] = j+1
            if t[i]==0:
                t[i]==i+1
            
                       
                   
    for j in range (len(t)):
        print(t[j])
