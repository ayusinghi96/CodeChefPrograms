n,k = map(int,input().split())
t = []
x = 0
for i in range(0,n):
    t.append(int(input()))
if k <= 10000000:
    for j in range(0,n):
        if t[j] % k == 0:
            x += 1
    print(x)


 

