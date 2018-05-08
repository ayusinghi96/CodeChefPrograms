t = int(input())
for i in range(0,t):
    b = []
    n = int(input())
    a = list(map(int,input().split()))
    print(a.index(min(a)) + 1)
    
