#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 18:00:30 2018

@author: shubham
"""
for _ in range(int(input())):
    g = int(input())
    for i in range(g):
        l,n,q = map(int, input().split())
        if n ==1:
            if l == q:
                print('0')
            else:
                print('1')
        else:
            if n%2 == 0:
                print(n//2)
            else:
                if l == 1:
                    if q ==1:
                        print(n//2)
                    else:
                        print(n//2+1)
                else:
                    if q ==2:
                        print(n//2)
                    else:
                        print(n//2+1)