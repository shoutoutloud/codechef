# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 23:46:34 2018

@author: shubham
"""
import itertools
def lcs(X , Y):
    
    m = len(X)
    n = len(Y)
    L = [[None]*(n+1) for i in range(m+1)]
 
    
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])
 
    
    return L[m][n]
for _ in range(int(raw_input())):
    N, M = map(int, raw_input().split())
    A = raw_input()
    B = raw_input()
    C = ''.join(ch for ch, _ in itertools.groupby(A))
    D = ''.join(ch for ch, _ in itertools.groupby(B))
    T = lcs(C, D)
    print(len(C)+len(D)-T)