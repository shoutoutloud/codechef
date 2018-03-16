#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 20:55:28 2018

@author: shubham
"""

n = int(input())
for _ in range(n):
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    d = len(a)-a[(len(a)-1)]
    print(d)