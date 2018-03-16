#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 23:58:33 2018

@author: shubham
"""
import itertools

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = []
    for l in range(n):
        a.append(int(input()))
    a.sort()
    s = []
    
    for i in range(1, n+1):
        s.append(list(itertools.combinations(a, i)))
#    if m in s:
#        print('Yes')
#    else:
#        print('No')
#1 2 4 8 16