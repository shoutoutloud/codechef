#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 20:38:05 2018

@author: shubham
"""

for _ in range(int(input())):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    D = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C =[]
    f1 = 0
    for i in range(n):
        C.append([A[i], D[i]])
        f1+=D[i]
    C.sort()
    if f1 != n:
        j = len(C)-1
        l = 0
        for i in range(k):
            f = f1-B[i]
            if (i+1)%2 == 0:
                while f>0:
                    if f-C[j][1]>=0:
                        f-=C[j][1]
                        j-=1
                    else:
                        w = C[j][1]
                        C[j][1]-=f
                        f-=w
            
            else:
            
                while f>0:
                    if f-C[l][1]>=0:
                        f-=C[l][1]
                        l+=1
                        
                    else:
                        w = C[l][1]
                        C[l][1]-=f
                        f-= w
            f1 = B[i]
            
        
         
        sum = 0
        if k%2==0:
            while l<=j and f1>=0:
                if f1-C[l][1]>0:
                    sum+=C[l][0]*C[l][1]
                    f1-=C[l][1]
                    l+=1
                else:
                    sum+=C[l][0]*f1
                    f1-=C[l][1]
            print(sum)
        else:
            while l<j and f1>=0:
                if f1-C[j][1]>0:
                    sum+=C[j][0]*C[j][1]
                    f1-=C[j][1]
                    j-=1
                else:
                    sum+=C[j][0]*f1
                    f1-=C[j][1]
        
            print(sum)
    else:
        A.sort()
        j = len(A)-1
        l =0
        f1 = n
        for i in range(k):
            f = f1-B[i]
            if (i+1)%2==1:
                A = A[f:]
            else:
                A = A[:len(A)-f]
            f1 = B[i]
        sum = 0
        
        for j in range(len(A)):
            sum+=A[j]
        print(sum)
            
            
            
            
            
            
            
            
            
            
            
                    