# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 18:59:03 2018

@author: shubham
"""
n = int(input())
a = list(map(int, input().split()))
s = []
size = 0
maxsize = 0
for i in range(n):
    if a[i]!=0:
        size+=1
        if size>=maxsize:
            maxsize = size
    else:
        if size>=maxsize:
            maxsize = size
        size = 0
print(maxsize)
            
        