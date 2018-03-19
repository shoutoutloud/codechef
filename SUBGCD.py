# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 14:56:02 2018

@author: shubham
"""
def gcd(a, b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    flag = 0
    g = a[0]
    for i in range(1, n):
        g = gcd(g, a[i])
        if g==1:
            flag = 1
            print(n)
            break   
    if flag == 0:
        print('-1')
    
            

        