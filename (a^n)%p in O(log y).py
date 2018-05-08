## Calculate (a ^ n) % p in O(logy)


def power(a,n,p):
    res = 1
    #if a >= p
    a = a % p
    
    while n > 0:
        if n & 1:
            res = (res * a) % p


        n = n >> 1 # n=n/2
        a = (a*a)%p
    return res


a = int(input())
n = int(input())
p = int(input())
print(power(a,n,p))

    
