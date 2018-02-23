#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 20:56:46 2018

@author: shubham
"""

n = int(input())
for _ in range(n):
    N = int(input())
    a = list(map(int, input().split()))
    b = []
    d = []
    a.sort()
    for j in range(N):
        d.append(a[j])
        d.append(a[N+j])
    for i in range(N):
        b.append(max(d[2*i+1], d[2*i]))
    print(b[((N+1)//2)-1])
    print(' '.join(map(str, d)),) 