for _ in range(int(input())):
    s, n = input().strip().split()
    n = int(n)
    count = 0
    cA = 0
    cB = 0
    if n<=1000:
        s*=n
        for i in s:
            if i=='a':  
                cA+=1
            else:
                cB+=1
            if cA>cB:
                count+=1
        print(count)
    else:
        t = s*1000
        for i in s:
            if i=='a':  
                cA+=1
            else:
                cB+=1
            if cA>cB:
                count+=1
        cA = 0
        cB = 0
        count1 = 0
        for i in t:
            if i=='a':  
                cA+=1
            else:
                cB+=1
            if cA>cB:
                count1+=1
        if s.count('a') == s.count('b'):
            print(count*n)
        elif s.count('a')<s.count('b'):
            print(count1)
        else:
            print(count1+(n-1000)*len(s))