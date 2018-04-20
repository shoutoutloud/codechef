# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 11:40:58 2018

@author: shubham
"""
def gcd(a, b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)
for _ in range(int(input())):
    n = 10**5
    A = [10**5]*10**5
    flag = 0
    g = 0
    for i in range(n):
        g = gcd(g, A[i])
        if g==1:
            print('-1')
            flag = 1
            break
    if flag ==0:
        for i in range(1, g+1):
            if gcd(g, i)!=1:
                print(i)
                flag = 1
                break
            
                
           
                