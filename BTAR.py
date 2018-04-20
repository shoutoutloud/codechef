# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 23:43:56 2018

@author: shubham
"""

for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().strip().split()))
    if sum(s)%4!=0:
        print('-1')
    else:
        c = 0
        for i in range(n):
            s[i] = s[i]%4
        t = s.count(1)
        u = s.count(3)
        if t==u:
            c+=(t+u)//2
            c+=s.count(2)//2
        elif t>u:
            if (t-u)%4!=0:
                c+=u
                t-=u
                c+=t//4*3+2+s.count(2)//2
            else:
                c+=u
                t-=u
                c+=t//4*3+s.count(2)//2
        else:
            if (u-t)%4!=0:
                c+=t
                u-=t
                c+=u//4*3+2+s.count(2)//2
            else:
                c+=t
                u-=t
                c+=u//4*3+s.count(2)//2
        print(c)