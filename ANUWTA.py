# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 12:39:05 2018

@author: shubham
"""
a = [0]*(10**5+1)
for i in range(1, 10**5+1):
    a[i]=a[i-1]+i
for _ in range(int(input())):
    n = int(input())
    count = 2*n+a[n-1]
    
    print(count)