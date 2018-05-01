# -*- coding: utf-8 -*-
"""
Created on Tue May  1 11:58:50 2018

@author: shubham
"""

for _ in range(int(input())):
    n = int(input())
    H = list(map(int, input().split()))
    K = list(map(int, input().split()))
    for i in range(n):
        H[i]*=2
    t = max(H)
    m = t+1
    ans = [m]*(t+1)
    ans[0] = 0
    for i in range(1,t+1):
        for j in range(n):
            if K[j]<=i and ans[i-K[j]]+1<ans[i]:
                ans[i]=ans[i-K[j]]+1
    count=0
    for i in range(n):
        count+=ans[H[i]]
    print(count) 