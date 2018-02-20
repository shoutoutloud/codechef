import sys
def maxSubArraySum(a,size):
      
    max_so_far = -sys.maxsize - 1
    max_ending_here = 0
      
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
 
        if max_ending_here < 0:
            max_ending_here = 0  
    return max_so_far
  
for _ in range(int(input())):
    N, K = map(int, input().split())
    s = list(map(int, input().split()))
    flag = 0
    if K==1:
        print(maxSubArraySum(s,len(s)))
        flag = 1
    else: 
        for i in range(len(s)):
            if s[i]<0 and sum(s)<=0:
                a = 2*s
                print(maxSubArraySum(a,len(a)))
                flag = 1
                break
            elif s[i]<=0 and sum(s)>0:
                a = 2*s
                print(maxSubArraySum(a,len(a))+sum(s)*(K-2))
                flag = 1
                break
    if flag ==0:
        print(int(K*sum(s))) 