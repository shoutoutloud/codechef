# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 16:34:35 2018

@author: shubham
"""

n = int(input())
s= list(map(int, input().split()))
q = int(input())
count = 0
for i in range(q):
    
    x,y = map(int, input().split())
    for k in range(n):
        if s[k]>0:
            if k&x == k:
                s[k] -= y
                if s[k] <=0:
                    count += 1
    print(n-count)