#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 20:48:24 2018

@author: shubham
"""

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    sum1 = 0
    if n<=2:
        for i in range(n):
            sum1+=a[i]
        print(sum1)
    else:
        
        for i in range(n-1, -1, -4):
            if i-1>=0:
                sum1+=a[i]+a[i-1]
            else:
                sum1+=a[i]
        print(sum1)
