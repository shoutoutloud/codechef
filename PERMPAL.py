#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 00:45:37 2018

@author: shubham
"""
for _ in range(int(input())):
    A = 'abcdefghijklmnopqrstuvwxyz'
    s = input()
    t = []
    flag = 0
    for i in range(len(s)):
        t.append(s[i]+str(i+1))
    t.sort()
    a = ''.join(t)
    t.clear()
    u = 0
    v = a[0]
    for i in range(1,len(a)):
        if a[i] in A and a[i] != v:
            t.append(a[u:i])
            u = i
            v = a[i]
        if i == len(a)-1:
            t.append(a[u:len(a)])
    count = 0
    center = ''
    for i in range(len(t)):
        c = 0
        for j in range(len(t[i])):
            if t[i][j] in A:
                c+=1
        if c%2!=0:
            count +=1
            if count>1:
                print('-1')
                flag = 1
                break
            else:
                center = t[i]
        if flag == 1:
            break
    if flag ==0:
         for i in range(len(t)):
            c = 0
            for j in range(len(t[i])):
                if t[i][j] in A:
                    c+=1
            if c%2==0:
                c1 = 0
                for j in range(len(t[i])):
                    
                    if t[i][j] in A:
                        
                        c1+=1
                        if c1==c//2+1:
                            
                            center = t[i][:j] + center + t[i][j:]
         p = ''
         for i in range(1,len(center)):
             if center[i]  in A:
                 if p!='':
                     print(int(p), end = ' ')
                 p = ''
             else:
                 p += center[i]
                 if i==len(center)-1:
                     print(int(p))
            