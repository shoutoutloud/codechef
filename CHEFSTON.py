# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 14:22:41 2018

@author: shubham
"""

for _ in range(int(input())):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    m = 0
    for i in range(n):
        t = k//A[i]
        if B[i]*t>m:
            m = B[i]*t
    print(m)