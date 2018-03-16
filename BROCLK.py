#import math
#from fractions import Fraction
mod = 10**9+7

def modInverse(a):
    m = mod
    m1 = mod
    if m==1:
        return 0
    x, y = 1, 0
    while a>1:
        q = a//m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t
    if x<0:
        x+= m1
    return x
    return 1
def pow1(A, B):
    x = (A[0][0]*B[0][0] +A[0][1]*B[1][0])%mod
    y = (A[0][0]*B[0][1]+A[0][1]*B[1][1])%mod
    z = (A[1][0]*B[0][0]+A[1][1]*B[1][0])%mod
    w = (A[1][0]*B[0][1]+A[1][1]*B[1][1])%mod
    A[0][0] = (x+mod)%mod
    A[0][1] =(y+mod)%mod
    A[1][0] = (z+mod)%mod
    A[1][1] = (w+mod)%mod

def power(A, B, n):
    
    while n>0:
        if n%2 != 0:
            pow1(A, B)
        pow1(B, B)
        n//=2
    
for _ in range(int(input())):
    l,d,t = map(int, input().split())
    p = ((d)*modInverse(l))%mod
    m = [[2*p,-1], [1, 0]]
    t1 = [[2*p,-1], [1, 0]]
    
    power(t1, m, t-1)
    
    ans =(t1[0][0]+t1[0][1]*p)%mod
    print((l*ans)%mod)
    