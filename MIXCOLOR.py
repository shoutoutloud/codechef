#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 22:43:55 2018

@author: shubham
"""
for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    count = 1
    A.sort()
    t = []
    for i in range(n-1):
        if A[i] == A[i+1]:
            count+=1
            if i == n-2:
                if count>1:
                    t.append(count-1)
        else:
            if count>1:
                t.append(count-1)
            count = 1
    count2 = 0
    for j in range(len(t)):
            count2+=t[j]
    print(count2)