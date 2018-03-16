#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 21:07:28 2018

@author: shubham
"""

for _ in range(int(input())):
    n = input()
    s = '0123456789'
    b = ''
    st = ''
    for i in s:
        if i in n:
            
            b+=i
    if '6' in b:
        k = 60
        for j in b:
            if int(j) == 6 and n.count('6')>1:
                st+=chr(66)
            elif int(j) >=5 and int(j)!=6:
                l = k+int(j)
                st+=chr(l)
    if '7' in b:
        k = 70
        for j in b:
            if int(j) == 7 and n.count('7')>1:
                st+=chr(77)
            elif int(j)!=7:                
                l = k+int(j)
                st+=chr(l)
    if '8' in b:
        k = 80
        for j in b:
            if int(j) == 8 and n.count('8')>1:
                st+=chr(88)
            elif int(j)!=8:                
                l = k+int(j)
                st+=chr(l)
    if '9' in b:
        if '0' in b:
            st+=chr(90)
    if len(st) == 0:
        print(" ")
    else:
        print(st) 