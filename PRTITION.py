# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 19:02:48 2018

@author: shubham
"""
def SplitSum(a, size, x):
    leftsum = 0
    s = []
    b = []
    sum1 = sum(a)
    flag = 0
    for i in range(size):
        leftsum += a[i]
        s.append(a[i])
    rightsum = 0
    for j in range(size):
        if rightsum + a[size-1-j]<=sum1/2 and sum1/2-(rightsum + a[size-1-j]) != x:     
            rightsum += a[size-1-j]
            b.append(a[size-1-j]-1)
            s[a[size-1-j]-1] = -1         
            if rightsum == sum1/2:
                for i in range(len(s)):
                    if s[i]>0:
                        a[i]=0
                for i in range(len(b)):
                    a[b[i]]=1
                flag = 1
                return a
                
    if flag ==0:
        return -1
for _ in range(int(input())):
    x, N =  map(int, input().split())
    a = []
    for i in range(N):
        a.append(i+1)
    a[x-1]=0
    if sum(a) %2 != 0:
        print('impossible')
    
    else:
        t = SplitSum(a, len(a), x)
        if t == -1:
            print('impossible')
        else:
            t[x-1] = 2
            print(''.join(map(str, t)))
            
            
        