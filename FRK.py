# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 12:40:23 2018

@author: shubham
"""
n = int(input())
a = ['ch','ef', 'he',]
b = []
for i in range(n):
    b.append(input().strip())
    count = 0
for i in b:
    for j in a:
        if j in i:
            count+=1
            break
print(count) 