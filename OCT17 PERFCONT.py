t = int(input())
for i in range(t):
    catwalk, hard = 0,0
    n,p = map(int,input().split())
    a = list(map(int,input().split()))
    for j in range(len(a)):
        if p//2 <= a[j]:
             catwalk += 1
        elif p//10 >= a[j]:
            hard += 1
    if catwalk == 1 and hard == 2:
        print("yes")
    else:
        print("no")
            
            
