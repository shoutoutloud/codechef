#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 20:53:57 2018

@author: shubham
"""

n = int(input())
for _ in range(n):
    N = int(input())
    hostel_id = set(map(int, input().split()))
    rank = list(map(int, input().split()))
    if len(hostel_id) > 1:
        print('No Party')
    else:
        rank.sort()
        if rank[0] < 15:
            print('No Party')
        else:
            print('Party')