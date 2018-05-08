a,b = map(int, input().split())
m = []
num = 0
if a > b:
    diff = a-b
##    print(diff)
    while diff != 0:
        mod = diff % 10
        m.append(mod)
        diff = diff // 10
    if m[0] < 9:
        m[0] = m[0] + 1
    else:
        m[0] -= 1
    for i in range(0,len(m)):
        num = num + 10**i * m[i]
    print(num)
