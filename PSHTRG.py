# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 15:30:54 2018

@author: shubham
"""

n, q = map(int, input().split())
A = list(map(int, input().split()))
for _ in range(q):
    a,l,r = map(int, input().split())
    if a==1:
        A[l-1] = r
    else:
        if r-l+1 <3:
            print('0')
        else:
            s = []
            for i in range(l-1, r):
                s.append(A[i])
            s.sort()
            ans = 0
            for i in range(len(s)-1, 1, -1):
                if s[i]<s[i-1]+s[i-2] and s[i-1]>s[i]-s[i-2]:
                    ans+=s[i]+s[i-1]+s[i-2]
                    break
            print(ans)