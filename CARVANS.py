# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 20:31:59 2018

@author: shubham
"""

for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    if n==1:
        print('1')
    else:
        count = 1
        min = A[0]
        for i in range(1,n):
            if A[i]<min:
                count+=1
                min=A[i]
        print(count)