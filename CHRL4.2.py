n,k = map(int,input().split())
a = list(map(int,input().split()))
a.insert(0,0)
y, pro,c = 1,1,1
##print(n,k,a)
while y < n:
    x = c
    y = c+1
    minimum = a[x]*a[y]
##    print("x,y:",x,y)
    while y-x <= k and 1 <= y-x and y <= n:
##        print("diff",y-x)
        product = a[x] * a[y]
##        print("product",product)
        if minimum < product and y == n or minimum >= product:
            minimum = product
            s = y
##            print("minimum and s",minimum,s)
##        else:
####            break
        y += 1
##        print("new y",y)
    y -= 1
    pro *= minimum // a[c]
##    print("final product",pro)
    c = s
##    print("new c:",c)

print((pro*a[1]) % 1000000007)
        
        
        
