# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 17:12:47 2018

@author: shubham
"""
def get_all_substrings(string):
  length = len(string)
  alist = []
  for i in range(length):
    for j in range(i,length):
      alist.append(string[i:j + 1]) 
  return alist
s = input()
q = int(input())
s1 = get_all_substrings(s)
t = ''.join(s1)
G = 0
for i in range (q):
    p,m = map(int, input().split())
    K = int((p*G)%m+1)
    G+= ord(t[K-1])
    print(t[K-1])