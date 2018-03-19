# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 13:40:16 2018

@author: shubham
"""
for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    t = sum(A)-max(A)
    u = sum(B)-max(B)
    if t<u:
        print("Alice")
    elif t>u:
        print("Bob")
    else:
        print("Draw")