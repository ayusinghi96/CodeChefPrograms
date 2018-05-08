def fact(x):
    if x == 0 or x == 1:
        return 1
    else:
        f = x * fact(x-1)
    return f



t = int(input())
for i in range(0,t):
    n = int(input())
    print(fact(n))


    
