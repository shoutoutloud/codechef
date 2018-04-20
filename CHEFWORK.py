# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 19:33:00 2018

@author: shubham
"""

n = int(input())
c = list(map(int, input().split()))
t = list(map(int, input().split()))
m1 = 0
m2 = 0
m3 = 0
for i in range(n):
    if t[i]==1:
        if m1==0:
            m1=c[i]
        else:
            if c[i]<m1:
                m1 = c[i]
    elif t[i] == 2:
        if m2==0:
            m2=c[i]
        else:
            if c[i]<m2:
                m2 = c[i]
    else:
        if m3==0:
            m3=c[i]
        else:
            if c[i]<m3:
                m3 = c[i]
if m1 == 0 or m2 == 0:
    print(m3)
elif m3 ==0:
    print(m1+m2)
else:
    print(min(m1+m2, m3))