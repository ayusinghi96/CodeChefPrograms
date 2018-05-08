t = int(input())
a = []
b = []
for i in range(0,t):
    a.append(input().split())
    b.append(input().split())
for i in range(0,t):
    x = 0
    m = a[i]
    n = b[i]
    for j in range(0,4):
        if m[j] in n:
            x += 1
    if x >= 2:
        print ('similar')
    else:
        print ('dissimilar')
