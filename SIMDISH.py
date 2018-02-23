#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 20:51:36 2018

@author: shubham
"""

n = int(input())
for _ in range(n):
    setA = set(input().split())
    setB = set(input().split())
    setC = set.intersection(setA, setB)
    if len(setC) >= 2:
        print('similar')
    else:
        print('dissimilar') 