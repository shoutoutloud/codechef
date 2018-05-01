# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 11:18:33 2018

@author: shubham
"""
from fractions import gcd
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if k>=max(a):
        print("YES")
    else:
        g = 0
        flag =0
        for i in range(n):
            g = gcd(g, a[i])
        if g<=k and k!=1:
            print("YES")
        elif g%k==0 and k!=1:
            print("YES")
        else:
            print("NO")