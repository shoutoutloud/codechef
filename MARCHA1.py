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
    sum = 0
    flag = 0
    for i in range(len(s)):
        for j in range(len(s[i])):
            for k in range(len(s[i][j])):
                sum+=s[i][j][k]
            if sum==m:
                print('Yes')
                flag = 1
                break
            else:
                sum = 0
        if flag == 1:
            break
    if flag==0:
        print('No')