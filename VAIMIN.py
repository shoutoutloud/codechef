# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 22:10:55 2018

@author: shubham
"""
def fact(n):
    if n == 1:
        return 1
    elif n ==0:
        return 1
    else:
        return n*fact(n-1)
p,q,c,m = map(int, input().split())
count  = 0
cG = c+1
cB = 0
if p<c and q>0:
    print('0')
    
else:
    for _ in range(p+q):
        if cG-(cB+1)>=c:
            if cB+1<=q:
                cB+=1
            else:
                break
        else:
            if cG+1<=p:
                cG+=1
                count+=q-cB
            else:
                count+=q-cB
                break
    t = []
    for _ in range(m):
        g, b = map(int, input().split())
        if g-b>=c and b<=q and g<=p and g>=c:
            if [g,b] not in t:
                t.append([g, b])
    if p<c and q == 0:
        if len(t)>0:
            print('0')
        else:
            print(p)
    else:
        s = p+q-c-1
        fa = fact(s)//(fact(p-c-1)*fact(q))
        print((fa-len(t)-count)%1000000007)

    