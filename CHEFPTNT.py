#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 23:44:31 2018

@author: shubham
"""
for _ in range(int(input())):
    n, m, x, k = map(int, input().split())
    s = input()
    if n>k:
        print('no')
    else:
        t = s.count('O')
        u = s.count('E')
        if m*x<n:
            print('no')
        else:
            if m%2!=0:
                if (m//2+1)*x<=t:
                    t = (m//2+1)*x
            else:
                if (m//2)*x<=t:
                    t = (m//2)*x
            if u>=(m//2)*x:
                u = (m//2)*x
            if t+u >=n:
                print('yes')
            else:
                print('no')
                