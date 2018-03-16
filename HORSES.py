#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 20:49:42 2018

@author: shubham
"""

n = int(input())
for _ in range(n):
    n = int(input())
    s = list(map(int, input().split()))
    s.sort()
    d = set()
    for i in range(n-1):
        d.add(abs(s[i+1]-s[i]))           
    print(min(d)) 