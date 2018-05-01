# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 01:13:47 2018

@author: shubham
"""
R = []
W = []
n =int(input())
for _ in range(n):
    r,w = map(int, input().split())
    R.append(r)
    W.append(w)

if W.count(10)>1:
    print("NO")
else:
    flag =0
    for i in range(1,n):
        if R[i]<R[i-1] or W[i]<W[i-1]:
            flag=1
            print("NO")
            break
    if flag==0:
        print("YES")