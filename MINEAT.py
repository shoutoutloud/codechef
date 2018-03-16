#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 11:21:54 2018

@author: shubham
"""
def bsearch(A, l, r, h):
    while l<r:
        mid = (l+r)//2
        count = 0
        for i in range(len(A)):
            count+=val(A[i], mid)
        if count<=h:
            r = mid
        else:
            l = mid+1
    return r
def val(x, i):
    if x%i!=0:
        return x//i+1
    else:
        return x//i
    
for _ in range(int(input())):
    n, h = map(int, input().split())
    A = list(map(int, input().split()))
    if n == h:
        print(max(A))
    else:
        ans = bsearch(A, 0, max(A), h)
        print(ans)
        
        