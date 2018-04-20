# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 21:40:20 2018

@author: shubham
"""
def f(N, K, ans, A, str1):
    if str1 == 'XOR':
        if K>0:
            if K%2==1:
                for j in range(N):
                    ans = ans^A[j]
    elif str1=='AND':
        if K>0:
            for j in range(N):
                ans = ans&A[j]
    else:
        if K>0:
            for j in range(N):
                ans = ans|A[j]
    return ans
for _ in range(int(input())):
    n, k, a = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))
    s = input().strip()
    print(f(n, k, a, A, s))