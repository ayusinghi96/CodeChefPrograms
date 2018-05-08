n,k = map(int,input().split())
m = n
a = list(map(int,input().split()))
a.insert(0,0)
print(n, k , a)
finalpro = 1
loops = n // k
print(loops)
for i in range(loops+1):
    print(i, "iteration")
    minimum = a[n]*a[n-1]
    print(minimum)
    for i in range(1,k+1):
        y = n-i
        if y > 0:
            x = n
            product = a[x]*a[y]
            print(y,x,product)
            if product < minimum:
                minimum = product
            print(minimum)
        else:
            break
            print("break")
    finalpro *= (minimum // a[n]) 
    print(finalpro)
    n = n-k
    print(n)
    
pro = a[1]*a[m]*finalpro
print(pro % 1000000007)

        
