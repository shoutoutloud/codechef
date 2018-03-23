# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 14:59:24 2018

@author: shubham
"""
from collections import OrderedDict
for _ in range(int(input())):
    A = input()
    B = input()
    a = ''.join(OrderedDict.fromkeys(A))
    count1 = 0
    for i in a:
        count1+=min(A.count(i),B.count(i))
    print(count1)
