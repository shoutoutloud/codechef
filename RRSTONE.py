# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 21:57:50 2018

@author: shubham
"""

N, K = map(int, input().split())
A = list(map(int, input().split()))
if K == 0:
    print(*A)
else:
    if K%2==0:
        for _ in range(2):
            m = max(A)
            for i in range(N):
                A[i] = m-A[i]
        print(*A)
    else:
        
        m = max(A)
        for i in range(N):
            A[i] = m-A[i]
        print(*A)