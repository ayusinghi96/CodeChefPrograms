import math
t = int(input())
for i in range(0,t):
    count = 0
    n = int(input())
    l = math.floor(math.log(n,5))
    for j in range(1,l+1):
        count = count + (n//5**j)
    print(count)
    
