# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 12:00:21 2018

@author: shubham
"""
import random
#def bsearch(a, l, r, x):
#    while l<=r:
#        mid = (l+r)//2
#        if a[mid] == x:
#            return 1
#        elif a[mid]>x:
#            r = mid-1
#        else:
#            l = mid+1
#    return 0
n, m, k = map(int, input().split())
A = list(map(int, input().split()))
P = list(map(int, input().split()))
#t = random.randint(1, k)
for i in range(n):
#    if bsearch(P, 0, m-1, A[i]+k) == 1:
#        A[i]+=k-1
#    else:
#        A[i]+=k
    A[i]+=k
print(*A)  