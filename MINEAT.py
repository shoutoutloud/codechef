#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 11:21:54 2018

@author: shubham
"""
for _ in range(int(input())):
    n, h = map(int, input().split())
    A = list(map(int, input().split()))
    if n == h:
        print(max(A))
    else:
        A.sort()
        t = h-n
        sum = 0
        for i in range(n):
            sum+=A[i]
        if sum%h!=0:
            sum1 = sum//h+1
        else:
            sum1 = sum//h
        if t <= n:
            print(max(sum1, A[n-1-t]))
        else:
            print(max(min(A), sum1))
        