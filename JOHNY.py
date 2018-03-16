#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 20:50:34 2018

@author: shubham
"""

n = int(input())
for _ in range(n):
    N = int(input())
    s = list(map(int, input().split()))
    k = int(input())
    z = s[k-1]
    s.sort()
    for i in range(len(s)):
        if s[i] == z:
            print(i+1) 