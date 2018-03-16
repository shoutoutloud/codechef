#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 21:03:32 2018

@author: shubham
"""

for _ in range(int(input())):
    s = list(map(int, input().split()))
    n = input()
    t = 'abcdefghijklmnopqrstuvwxyz'
    count = 0
    for i in range(len(t)):
        if t[i] not in n:
            count += s[i]
    print(count) 