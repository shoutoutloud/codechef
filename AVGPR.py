# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 18:06:40 2018

@author: shubham
#"""

def sum1(x1):
    s = 0
    for i in range(1,x1):
        s+=i
    return s
def bsearch(a, l, r, x):
    while l<=r:
        mid = (l+r)//2
        if a[mid]==x:
            return 1
        elif a[mid]>x:
            r=mid-1
        else:
            l = mid+1
    return 0
for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    count=0
    s = [0]*(2001)
    for i in A:
        s[1000+i]+=1
    t = []
   
    for i in A:
        if i not in t:
            t.append(i)
    size = len(t)
    for i in range(size-1):
        for j in range(i+1, size):
            if bsearch(t, 0, size-1, 2*t[i]-t[j]) == 1:
                count+=s[1000+2*t[i]-t[j]]*s[1000+t[j]]
    
    for i in range(len(s)):
        if s[i]>0:
            count+=sum1(s[i])

    print(count)
