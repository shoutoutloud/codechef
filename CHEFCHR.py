#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 01:12:50 2018

@author: shubham
"""
for _ in range(int(input())):
    s = input()
    count = 0
    t= ''
    for i in range(len(s)-3):
        t = s[i]+s[i+1]+ s[i+2]+s[i+3]
        if 'c' in t and 'h' in t and 'e' in t and 'f' in t:
            count+=1
    if count>0:
        print('lovely', count)
    else:
        print('normal')