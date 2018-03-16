#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 19:38:20 2018

@author: shubham
"""
for _ in range(int(input())):
    n, u, d = map(int, input().split())
    a = list(map(int, input().split()))
    count = 1
    flag = 0
    if n <=1:
        print('1')
    else:
        count2 = 0
        for i in range(n-1):
            if a[i+1]>=a[i]:
                if a[i+1]-a[i]<=u:
                    count = i+2
                else:
                    print(count)
                    flag = 1
                    break
            else:
                if a[i]- a[i+1] <=d:
                    count = i+2
                else:
                    if count2 == 0:
                        count2 += 1
                        count = i+2
                    else:
                        print(count)
                        flag = 1
                        break
        if flag == 0:
            print(count)