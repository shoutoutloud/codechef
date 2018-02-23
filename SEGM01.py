#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 20:53:18 2018

@author: shubham
"""

n = int(input())
for _ in range(n):
    s = input()
    if '1' not in s:
        print('NO')
    for i in range(len(s)):
        if s[i] == '1':
            s = s[i:]
            if '01' in s:
                print('NO')
                break
            else:
                print('YES')
                break 