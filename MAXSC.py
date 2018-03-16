# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 15:05:28 2018

@author: shubham
"""

for _ in range(int(input())):
    A = []
    sum = 0
   
    N = int(input())
    for i in range(N):
        s = list(map(int, input().split()))
        s.sort()
        A.append(s)
    E = A[N-1][N-1]
    sum += E
    for i in range(N-1):
        flag = 0
        for j in range(N):
            if A[N-i-2][N-1-j]<E:
                E = A[N-i-2][N-1-j]
                sum += E
                flag = 1
                break
        if flag ==0:
            break
    if flag == 0:
        print('-1')
    else:
        print(sum)
        
    
        
            