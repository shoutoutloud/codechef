# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 20:49:47 2018

@author: shubham
"""

for _ in range(int(input())):
    n, x = map(int, input().split())
    A = list(map(int, input().split()))
    m = min(A)
    s = sum(A)
    if s<x:
        print('-1')
    else:
        k = s//x
        r = s%x
        if r>=m:
            print('-1')
        else:
            print(k)
        