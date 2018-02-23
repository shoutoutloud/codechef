#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 18:27:05 2018

@author: shubham
"""
def SegTree(a,st, s, e, curr):
    if s==e:
        st[curr] = a[s]
        return st[curr]
    mid = (s+e)//2
    st[curr] = max(SegTree(a, st, s, mid, 2*curr+1), SegTree(a, st, mid+1, e, 2*curr+2))
    return st[curr]


def ans(st, s,e, qs, qe, curr):
    if qs<=s and qe>=e:
        return st[curr]
    if e<qs or s>qe:
        return 0
    mid = (s+e)//2
    return max(ans(st, s, mid, qs, qe, 2*curr+1), ans(st, mid+1, e, qs, qe, 2*curr+2))

n, k, b = map(int, input().split())
A = list(map(int, input().split()))
sum2 = 0
for i in range(n):
    sum2+=A[i]
p = input()
seg = [0]*(10*n)
count = 0
B = 2*A
sum1 = [0]*(2*n)
sum1[0] = B[0]
for i in range(1,k):
    sum1[i] = sum1[i-1] + B[i]
for i in range(k, 2*n):
    sum1[i] = sum1[i-1]+B[i]-B[i-k]
SegTree(sum1, seg, 0, 2*n-1, 0)
count = 0
for i in p:
    if i == '?':
        if k<n:
            if count==0:
                print(ans(seg, 0,2*n-1, 0,n-1, 0))
            else:
                print(ans(seg, 0, 2*n-1, n-count+k-1, 2*n-1-count, 0))
        else:
            print(sum2)
    else:
        count+=1
        count%=n


    