#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 20:54:46 2018

@author: shubham
"""

n = int(input())
for _ in range(n):
    s = input()
    if 'SE' in s:
        print('no')
    elif 'SC' in s:       
        print('no')
    elif 'EC' in s:
        print('no')
    else:
        print('yes') 