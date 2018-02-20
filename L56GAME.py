#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 20:22:55 2018

@author: shubham
"""
for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    count = 0
    if n==1:
        print('1')
    else:    
        for i in range(n):
            if A[i] %2 != 0:
                count+=1
        if count%2!=0:
            print('2')
        else:
            print('1')