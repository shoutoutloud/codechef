#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 21:16:06 2018

@author: shubham
"""
for _ in range(int(input())):
    N,R = map(int, input().split())
    A = list(map(int, input().split()))
    flag = 1
    t1 = R
    t2 = -1
    for i in range(N-2):
        if A[i] >R:
            t1 = A[i]
            if t1 != R and A[i+1]>t1:
                flag = 0
                break
            elif A[i+1]<t2:
                flag = 0
                break
        elif A[i]<R: 
            t2 = A[i]
            if t1 != R and A[i+1]>t1:
                flag = 0
                break
            elif A[i+1]<t2:
                flag = 0
                break
        
    if flag ==0:
        print('NO')
    else:
        print('YES') 
