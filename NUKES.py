# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 15:44:56 2018

@author: shubham
"""
a,n,k=map(int,input().split(" "))
for _ in range(k):
    print(a%(n+1),end = " ")
    a=a//(n+1) 
    