t = int(input())
for i in range(t):
    a, b = input().split()
    a = '0'*(10-len(a)) + a
    b = '0'*(10-len(b)) + b
    c = ''
    for j in range(10):
        c += str(int(a[j]) + int(b[j]))[-1:]
    print(int(c))
