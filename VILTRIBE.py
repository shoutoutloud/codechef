#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 21:09:02 2018

@author: shubham
"""

for _ in range(int(input())):
    s = input()
    countA = 0
    countB = 0
    countA+=s.count('A')
    countB+=s.count('B')
    for i in range(len(s)):
        if s[i] == 'A':
            A = []
            for j in range (i+1,len(s)):
                
                if s[j] == 'A':
                    countA += len(A)
                    break
                elif s[j] == 'B':
                    A.clear()
                    break
                else:
                    A.append(s[j])
        if s[i] == 'B':
            B = []
            for j in range (i+1,len(s)):
                
                if s[j] == 'B':
                    countB += len(B)
                    break
                elif s[j] == 'A':
                    B.clear()
                    break
                else:
                    B.append(s[j])
    print (countA,countB)