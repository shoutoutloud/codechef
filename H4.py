#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 00:52:43 2018

@author: shubham
"""
import math
for _ in range(int(input())):
    n, m = map(int, input().split())
    sum = 0
    for i in range(n%m):
        sum += math.pow(i+1,i+1)
    print(int(sum%m))