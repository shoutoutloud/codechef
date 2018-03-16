# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 00:43:16 2018

@author: shubham
"""
for _ in range(int(input())):
    N = int(input())
    S = list(map(int, input().split()))
    t = [0]*N
    if N ==1:
        print('0')
    else:
        s = [0]*N
        
        for i in range(0, N):
            sum = 0
            for j in range(i+1, N):
                if sum<=S[i]:
                    s[j]+=1
                    sum+=S[j]
                else:
                    break
            sum = 0
            for j in range(i-1, -1, -1):
                if sum<=S[i]:
                    s[j]+=1
                    sum+=S[j]
                else:
                    break
        print(*s)
    
        