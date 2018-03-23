# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 13:48:33 2018

@author: shubham
"""
n = int(input())
while n!=0:
    L = list(map(int, input().split()))
    L.sort()
    count =0
    for i in range(n-1, 1, -1):
        j = 0
        k = i-1
        while j<k:
            if L[j]+L[k]<L[i]:
                count+=k-j
                j+=1
            else:
                k-=1
    print(count)
    n = int(input())
                    