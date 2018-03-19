# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 14:49:09 2018

@author: shubham
"""
for _ in range(int(input())):
    n,m=list(map(int,input().split()))
    M=[]
    flag=0
    for i in range(n):
    	b=list(map(int, input().split()))
    	M.append(b)   
    for i in range(n):
        min1 = 0
        for j in range(m):
            if M[i][j]!=-1:
                if M[i][j]<min1:
                    flag = 1
                    print('-1')
                    break
                else:
                    min1 = M[i][j]
        if flag ==1:
            break
    if flag ==0:       
        for i in range(m):
            min1 = 0
            for j in range(n):
                if M[j][i]!=-1:
                    if M[j][i]<min1:
                        flag = 1
                        print('-1')
                        break
                    else:
                        min1 = M[j][i]
            if flag ==1:
                break
    if flag == 0:
        min1 = min(M[0])
        if M[0][0]==-1:
            M[0][0] = 1
        for i in range(m):
            if M[0][i] == -1:
                M[0][i] = min1
            else:
                if M[0][i]>=min1:
                    min1=M[0][i]
        for i in range(1, n):
            min1 = min(M[i])
            for j in range(m):
                if M[i][j] ==-1:
                    M[i][j] = max(M[i-1][j], min1)
                else:
                    min1= max(min1, M[i][j])
        for i in range(n):
            min1 = 0
            for j in range(m):
                
                if M[i][j]<min1:
                    flag = 1
                    print('-1')
                    break
                else:
                    min1 = M[i][j]
            if flag ==1:
                break
        if flag ==0:       
            for i in range(m):
                min1 = 0
                for j in range(n):
                    if M[j][i]<min1:
                        flag = 1
                        print('-1')
                        break
                    else:
                        min1 = M[j][i]
                if flag ==1:
                    break
            if flag ==0:
                for i in range(n):
                    T = M[i]
                    print(*T)
            
        
                
            
                