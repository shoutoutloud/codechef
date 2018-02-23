#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 20:58:56 2018

@author: shubham
"""

for _ in range(int(input())):
    flag=0
    N, d = map(int, input().split())
    s = list(map(int, input().split()))   
    count =0
    m =0
    for l in range(N):
        m = m+s[l]
    if m%len(s)!=0:
        print('-1')
    else:
        flag = 0        
        x = m/len(s)                    
        for a in range(d):       
            k = 0
            p = 0
            z = a
            while z<N:
                k+=s[z]                
                p+=1
                z+=d
            if k %p ==0 and k/p==x:
                flag = 0
            else:                               
                flag=1
                break
        if flag ==1:
            print('-1')
        else:
            for i in range(d):
                c=1
                j=i
                sum=0
                while j<N:
                    sum=sum+s[j]
                    count+=abs(x*c-sum)
                    j+=d
                    c+=1    
            print(int(count)) 