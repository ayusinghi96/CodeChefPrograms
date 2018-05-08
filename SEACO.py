def first():
    global querry, a
    for i in range(querry[1][k],querry[2][k]):
        a[i] += 1
    print(a)


t = int(input())
for i in range(0,t):
    querry,a = [],[]
    n,q = input().split()
    n = int(n)
    for j in range(0,n):
        a.append(0)
##    print(a)
    q = int(q)
    for j in range(0, q):
        querry.append(list(map(int,input().split())))
##    print(querry)
    for k in range(0,q):
        if querry[0][k] == 1:
            first()
