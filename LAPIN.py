#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 20:43:28 2018

@author: shubham
"""
for _ in range(int(input())):
    s = input()
    flag = 0
    if len(s) %2 == 0:
        t = s[:len(s)//2]
        u = s[len(s)//2:]
    else:
        t = s[:len(s)//2]
        u = s[1+len(s)//2:]
    for i in t:
        if i not in u:
            flag = 1
            break
        elif t.count(i) != u.count(i):
            flag =1
            break
    if flag == 1:
        print('NO')
    else:
        print('YES')