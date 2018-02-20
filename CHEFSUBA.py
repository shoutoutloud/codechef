#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 18:27:05 2018

@author: shubham
"""
n, k, b = map(int, input().split())
A = list(map(int, input().split()))
max1 = 0
for i in range (n-2):
    sum1 = A[i]+A[i+1]+A[i+2]
    if sum1 >max1:
        max1 = sum1
    if max1 == 3:
        break
p = input()
t = p.count('!')
if t > n:
    t = t%n
s = []
for i in range(t):
    A = A[-1:] +A[:-1]
    max2 = 0
    for i in range (n-2):
        sum2 = A[i]+A[i+1]+A[i+2]
        if sum1 >max2:
            max2 = sum2
        if max2 == 3:
            break
    s.append(max2)
count = 0
for j in p:
    if j == "!":
        count+=1
    else:
        if count == 0:
            print(max1)
        else:
            print(s[count-1])
    