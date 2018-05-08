t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    k = int(input())
    store = a[k-1]
    a.sort()
    for i in range(n):
        if a[i] == store:
            print(i+1)
        
