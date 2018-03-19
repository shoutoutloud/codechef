# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 11:36:34 2018

@author: shubham
"""

for _ in range(int(input())):
    L, D, S, C = map(int, input().split())
    flag=0
    for i in range(D):
        if S>=L:
            print("ALIVE AND KICKING")
            flag = 1
            break
        else:
            S*=(1+C)
    if flag ==0:
        print("DEAD AND ROTTING")