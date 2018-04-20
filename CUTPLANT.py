# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 00:43:50 2018

@author: shubham
"""
from collections import deque
for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    flag = 0
    for i in range(n):
        if B[i]>A[i]:
            print('-1')
            flag = 1
            break
    if flag==0:
        count = 0
        t = deque()
#        max1 = 0
#        min1 = B[0]
        for i in range(n):
            
            
            while t and t[0]>A[i]:
                t.popleft()
            while t and t[-1]<B[i]:
                t.pop()
            if not t and A[i]!=B[i]:
                t.append(B[i])
                count+=1
            elif t and t[-1] != B[i] and A[i]!=B[i]:
                t.append(B[i])
                count+=1
        print(count)