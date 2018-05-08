t = int(input())
for i in range(t):
    todo = []
    a,q,r = [],[],[]
    n,m = map(int, input().split(" "))
    done = list(map(int, input().split(" ")))
##    print(done)
    a.append(0)
    q.append(0)
    r.append(0)
    
    for i in range(1,n+1):
        a.append(i)
##    print(a)
    for i in done:
        a.remove(i)
    print(a)
    for i in range(1,len(a)):
        if i % 2 == 0:
            q.append(i)
        else:
            r.append(i)
    for i in range(1,len(r)):
        print(r[i], end = " ")
    print()
    for i in range(1,len(q)):
        print(q[i], end = " ")
    print()
