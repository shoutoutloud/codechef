# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 20:05:47 2018

@author: shubham
"""
for _ in range(int(input())):
    n = int(input())
    flag = 0
    if n==1:
        print('2')
    else:
        for i in range(1,31):
            if (2**i)-1==n:
                flag=1
                t = i
                break
        if flag == 0:
            print('-1')
        else:
            print(2**(t-1)-1)
        