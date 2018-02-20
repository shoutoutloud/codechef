#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 12:59:45 2018

@author: shubham
"""
for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    c, d, s = map(int, input().split())
    print(max(A)*((c-1)))