# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 12:19:15 2018

@author: shubham
"""

n, d = map(int, input().split())
L = []
for i in range(n):
    L.append(int(input()))
L.sort()
if n==1:
    print('0')
else:
    i = n-1
    count = 0
    while i>0:
        if L[i]-L[i-1]>d:
            i-=1
        else:
            count+=1
            i-=2
    print(count)
    