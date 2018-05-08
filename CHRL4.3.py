import math
n,k = map(int,input().split())
a = list(map(int,input().split()))
a.insert(0,0)
c,y,pro = 1,1,1
b = []
b.append(a[1])
while y < n:
    x = c
    y = c+1
    smallest = math.inf
##    print("x,y,smallest", x,y,smallest)
    while y-x >= 1 and y-x <= k and y <= n:
        if a[y] <= smallest or a[y] >= smallest and y == n:
            smallest = a[y]
##            print("small", smallest)
            s = y
        y += 1
##        print(y)

    y -= 1
##    print("new y", y)
    b.append(a[s])
##    print(b)
    c = s
for i in range(len(b)):
    pro *= b[i]
##    print(pro)
print(pro % 1000000007)

    
        
        
