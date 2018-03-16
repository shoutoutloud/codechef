#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 20:46:50 2018

@author: shubham
"""

n = int(input())
for _ in range(n):
    N = int(input())
    if 360 % N == 0:
        ans = 'y'
    else:
        ans = 'n'
    if N <= 360:
        ans1 = 'y'
    else:
        ans1 = 'n'
    if (N*(N+1)/2) <= 360:
        ans2 = 'y'
    else:
        ans2 = 'n'
    print(ans, ans1, ans2) 