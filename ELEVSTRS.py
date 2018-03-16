#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 20:59:42 2018

@author: shubham
"""

for _ in range(int(input())):
    N, V1, V2 = map(int, input().split())
    i = 2**(1/2)*N/V1
    j = 2*N/V2
    if i < j:
        print('Stairs')
    else:
        print('Elevator') 