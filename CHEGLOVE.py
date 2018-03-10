#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 21:25:28 2018

@author: shubham
"""
for _ in range(int(input())):
    n = int(input())
    L = list(map(int, input().split()))
    G = list(map(int, input().split()))
    s=[]
    t = []
    for i in range(n):
        s.append(G[i]-L[i])
        t.append(G[i]-L[n-i-1])
    count = 0
    for j in s:
        if j<0:
            count = 1
            break
    count1 = 0
    for k in t:
        if k <0:
            count1 = 1
            break
    if count ==0 and count1 == 0:
        print('both')
    elif count == 0 and count1 == 1:
        print('front')
    elif count ==1 and count1 ==0:
        print('back')
    else:
        print('none')