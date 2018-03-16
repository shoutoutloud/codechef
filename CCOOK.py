#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 22:44:57 2018

@author: shubham
"""

n = int(input())
for _ in range(n):
    a = list(map(int, input().split()))
    sum1 = 0
    for i in range (len(a)):
        sum1 += a[i]
    if sum1 == 0:
        print('Beginner')
    elif sum1 == 1:
        print('Junior Developer')
    elif sum1 == 2:
        print('Middle Developer')
    elif sum1 == 3:
        print('Senior Developer')
    elif sum1 == 4:
        print('Hacker')
    elif sum1 == 5:
        print('Jeff Dean')