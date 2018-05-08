from collections import deque
from math import log
n, k = map(int, input().split())
l = list(map(int, input().split()))
print("Initial list",l)
a = list(map(log, l))
print("List after lg",a)
b = [-1]
d = deque()
print("d:", d)
d.append(0)
print("New d:", d)
for i in range(1, n):
    while d[0] < i - k:
        d.popleft()
        print("d after poping:", d)
    a[i] += a[d[0]]
    print("a:",a[i])
    b.append(d[0])
    print("b:", b)
    while d and a[d[-1]] >= a[i]:
        d.pop()
        print("d:",d)
    d.append(i)
    print("d:", d)
c = 1
a = n - 1
while a >= 0:
    c = (c * l[a]) % 1000000007
    a = b[a]
print(c) 
