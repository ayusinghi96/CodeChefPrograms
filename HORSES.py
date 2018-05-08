t = int(input())
for i in range(t):
    a = []
    n = int(input())
    s = list(map(int,input().split()))
    s.sort()
##    print(s)
    for i in range(n-1):
        a.append(s[i+1] - s[i])
    a.sort()
    print(a[0])
