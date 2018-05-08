def mergesort(x,p,r):    
    import math
    if p < r:
        q = math.floor((p+r)/2)
        mergesort(x,p,q)
        mergesort(x,q+1,r)
        merge(x,p,q,r)
    print(x)

def merge(m,p,q,r):
    L = []
    R = []   
    n1 = q-p+1
    n2 = r-q
    
    for i in range(1,n1+1):
        L.append(m[(p+i-1)])
    for i in range(1,n2+1):
        R.append(m[q+i])
    
    i,j = 0,0
    for k in range(p,r):
        if L[i] <= R[j]:
            m[k] = L[i]
            i += 1
        else:
            m[k] = R[j]
            j += 1
    
        
t = int(input())
a = []
for i in range(0,t):
    a.append(int(input()))
p = 0
r = t
mergesort(a,p,r)
##print(a)
