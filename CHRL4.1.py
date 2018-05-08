n,k = map(int,input().split())
b = n
a = list(map(int,input().split()))
a.insert(0,0)
pro = 1
y = 1
while y > 0:
    minimum = a[n]*a[n-1]
    for i in range(1,k+1):
        y = n-i
        if y > 0:
            x = n
            product = a[x]*a[y]
            if product < minimum:
                minimum = product
                s = n-i
        else:
            break

    pro *= (minimum // a[n])
    n = s
    
finalPro = a[b]*pro
print(finalPro % 1000000007)
