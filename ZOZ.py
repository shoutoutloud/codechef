# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 12:41:14 2018

@author: shubham
"""

for _ in range(int(input())):
    n, k = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))
    s = sum(A)
    A.sort()
    count = 0
    for i in range(n-1, -1, -1):
        if A[i]+k>s-A[i]:
            count+=1
        else:
            break
    print(count) 