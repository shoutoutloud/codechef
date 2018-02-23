#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 20:49:19 2018

@author: shubham
"""

n = int(input())
for _ in range(n):
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    x = []
    s = []
    ns= []
    for i in range(1, n+1):
        if i not in l:
            x.append(i)
        else:
            continue
    x.sort()
    for j in range(0, len(x), 2):
        s.append(str(x[j]))
    for k in range(1, len(x), 2):
        ns.append(str(x[k]))
    print(' '.join(s))
    print(' '.join(ns)) 