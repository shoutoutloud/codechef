#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 15:55:15 2018

@author: shubham
"""

for _ in range(int(input())):
    s = []
    for i in range(int(input())):
        s.append(list(map(int, input().split())))
    for t in range(int(input())):
        m = list(map(int, input().split()))
        
        c1 = 0
        for i in range(len(s)):
            count = 0
            for j in range(1,len(m)):
                if s[i][0] <= m[j] and m[j]<=s[i][1]:
                    count+=1    
            if count%2!=0:         
                c1+=1
        print(c1)
    
    