# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 14:43:11 2018

@author: shubham
"""
for _ in range(int(input())):
    a,b,c,d = map(int, input().split())
    s= []
    s.append(a)
    s.append(c)
    s.append(b)
    s.append(d)
    if s.count(a)%2!=0 or s.count(b)%2!=0 or s.count(c)%2!=0 or s.count(d)%2!=0:
        print('NO')
    else:
        print('YES')