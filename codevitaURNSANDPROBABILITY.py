M,X = map(int,input().split())
a,b,c=[],[],[]
s = 0
for i in range(0,M):
    a.append(int(input()))
for i in range(0,M):
    s = s + a[i]
if(X < s):
    print("Thank you,your order for "+ str(X)+ " eggs is accepted")
    for i in range(0,M):
        if(X > a[i]):
            X = X - a[i]
            b.append(a[i])
            c.append(a[i]-b[i])
        else:
            b.append(X)
            X = 0
            c.append(a[i]-b[i])
    for i in range(0,M):
        print (str(a[i]) + "\t" + str(b[i]) + "\t" + str(c[i]))
else:
    print("Sorry, we can only supply "+ str(s-1) +" eggs")
    for i in range(0,M-1):
        if(X > a[i]):
            X = X - a[i]
            b.append(a[i])
            c.append(a[i]-b[i])
        else:
            b.append(X)
            X = 0
            c.append(a[i]-b[i])
    for i in range(0,M-1):
        print (str(a[i]) + "\t" + str(b[i]) + "\t" + str(c[i])) 
    print (str(a[M-1]) + "\t" + str(a[M-1]-1) + "\t" + str(1))

