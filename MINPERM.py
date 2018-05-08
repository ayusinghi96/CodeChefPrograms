t = int(input())
for i in range(0,t):
    n = int(input())
    if n % 2 is 0:
        a = []
        for j in range(1,n,2):
            a.append(j+1)
            a.append(j)
        a.reverse()
        for j in range(1,n+1):
            print(a.pop(),end=' ')
        print()
    else:
        a = []
        for j in range(1,n-3,2):
            a.append(j+1)
            a.append(j)
        a.append(n-1)
        a.append(n)
        a.append(n-2)
        a.reverse()
        for j in range(1,n+1):
            print(a.pop(),end=' ')
        print()
            
