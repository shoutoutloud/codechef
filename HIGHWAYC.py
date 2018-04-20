# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 11:41:40 2018

@author: shubham
"""
for _ in range(int(input())):
    n, s, y = map(int, input().split())
    V = list(map(int, input().split()))
    D = list(map(int, input().split()))
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    count = 0
    t1 = y/s
    for i in range(n):
        if P[i] == 0:
            if count<(C[i]+0.000001)/V[i]:
                count = (C[i]+0.000001)/V[i]+t1
            else:
                count+=t1
        elif D[i]==0 and P[i]>0:
            d = P[i]-0.000001
            t2 = d/V[i]
            if (count+t1)>t2 and (count)<(P[i]+C[i]+0.000001)/V[i]:
                count=t1+(P[i]+C[i]+0.000001)/V[i]
            else:
                count+=t1
        elif D[i]==1 and P[i]<0:
            d = abs(P[i])-0.000001
            t2 = d/V[i]
            if (count+t1)>t2 and (count)<(abs(P[i])+C[i]+0.000001)/V[i]:
                count=((abs(P[i])+C[i]+0.000001)/V[i])+t1
            else:
                count+=t1
        elif D[i]==1 and P[i]>0 and (C[i]-P[i]+0.000001)/V[i]>count:
            count = (C[i]-P[i]+0.000001)/V[i]+t1
        elif D[i]==0 and P[i]<0 and (C[i]-abs(P[i])+0.000001)/V[i]>count:
            count+=t1+(C[i]-abs(P[i])+0.000001)/V[i]
        else:
            count+=t1
    print ('{0:.6f}'.format(count))
    