#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 21:00:26 2018

@author: shubham
"""

for _ in range(int(input())):
    k, a, b = map(int, input().split())
    if abs(b-a)==k/2:
        print('0')
    elif abs(b-a)<k/2:
        print(abs(b-a)-1)
    else:
        print(k-abs(b-a)-1) 