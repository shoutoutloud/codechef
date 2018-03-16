#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 20:52:34 2018

@author: shubham
"""

n = int(input())
for _ in range (n):
    a, b = map(int, input().split())
    if b==1:
        print('Limak')
    else:
        l = 0
        bob = 0
        num = 1
        count = 2
        while l+num<= a:
            l += num
            num += 2
        while bob+ count <= b:
            bob += count
            count += 2
        if num > count:
            print('Limak')
        else:
            print('Bob') 