# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 20:10:01 2018

@author: shubham
"""
n, k, p = map(int, input().split())
A = list(map(int, input().split()))
b = []
for i in range(n):
    b.append([A[i], i])
b.sort()
count = 0
ind = [-1]*n
ind[b[0][1]] = count
for i in range(1,n):
    if b[i][0]-b[i-1][0]>k:
        count+=1
    ind[b[i][1]]=count

for _ in range(p):
    a, b= map(int, input().split())
    if ind[a-1]==ind[b-1]:
        print('Yes')
    else:
        print('No')
        