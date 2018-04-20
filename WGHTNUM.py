# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 15:42:06 2018

@author: shubham
"""
mod = 10**9+7
def power(a, N):
    if N==0:
        return 1
    elif N==1:
        return a
    else:
        r = power(a, N//2)
        if N%2 == 0:
            return ((r%mod)*(r%mod))%mod
        else:
            return ((r%mod)*a*(r%mod))%mod
for _ in range(int(input())):
    n, w = map(int, input().strip().split())
    n = n-2
    
    if w>8 or w<-9:
        print('0')
    elif w>=0:
        t = 9-w
        ans=t*(power(10, n))
        print(int(ans)%mod)
    else:
        t = 10+w
        ans=t*(power(10, n))
        print(int(ans)%mod)