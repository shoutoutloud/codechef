# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 19:41:25 2018

@author: shubham
"""

n, q = map(int, input().split())
A = list(map(int, input().split()))
for i in range(n):
    t = bin(A[i])
    A[i]= t[2:]
for i in range(len(A)):
    A[i] = '0'*(31-len(A[i]))+A[i]
sum1 = [[[0 for k in range(2)] for j in range(31)] for i in range(n+1)]

for i in range(31):
    s1 = 0
    s2 = 0
    for j in range(n):
        if A[j][i] == '1':
            s1+=1
        else:
            s2+=1
        sum1[j+1][i][0] = s2
        sum1[j+1][i][1] = s1

for _ in range(q):
    L, R = map(int, input().split())
    x = ''
    for i in range(31):
        if sum1[R][i][0]-sum1[L-1][i][0]>sum1[R][i][1]-sum1[L-1][i][1]:
            x+='1'
        else:
            x+='0'
    sum = 0
    for i in range(len(x)-1, -1, -1):
        sum+=(2**i)*int(x[len(x)-1-i])
    print(sum)