#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 21:50:38 2018

@author: shubham
"""
for _ in range(int(input())):
    m = []
    n = int(input())
    for i in range(n):
        m.append(list(map(int, input().split())))
    count = 0
    for j in range(n):
        t = m[j][0]
        m[j][0] += m[j][0]*m[j][2]/100
        m[j][0] -= m[j][0]*m[j][2]/100
        count += (t-m[j][0])*m[j][1]
    print(count)