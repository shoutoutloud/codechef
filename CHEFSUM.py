#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 21:04:58 2018

@author: shubham
"""

for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    t = min(s)
    for i in range(len(s)):
        if s[i] == t:
            print(i+1)
            break 