#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 20:47:35 2018

@author: shubham
"""

import random
L = '0123456789'
A, B = input().split()
C = int(A)-int(B)
D = int(random.choice(L))
E = C%10
if D == E:
    while D==E:
         D = int(random.choice(L))   
    C = C-E+D
else:
    C = C-E+D
print(C)