# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 02:33:34 2018

@author: shubham
"""
for _ in range(int(input())):
    x,y,k,n = map(int, input().split())
    p = []
    for i in range(n):
        a, b = map(int, input().split())
        p.append([a, b])
    flag = 0
    for i in range(n):
        if p[i][0]>=x-y:
            t = p[i][1]
            if t<=k:
                print("LuckyChef")
                flag=1
                break
    if flag == 0:
        print("UnluckyChef")
    