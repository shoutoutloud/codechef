#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 22:29:23 2018

@author: shubham
"""
for _ in range(int(input())):
    n, k, b = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    i = 1
    count=0
    curr = A[0]
    while i<n:
        if curr*k+b<=A[i]:
            count+=1
            curr = A[i]
        i+=1
    print(count+1)