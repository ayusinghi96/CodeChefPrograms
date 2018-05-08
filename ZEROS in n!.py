'''no. of zeros in n!
    first find the power of 5 which is possible before nusing log(n,5) function.
    then we find no.of 5 available till n using (n/5**i)'''

def zeros(n):
    import math
    l = math.floor(math.log(n,5))
    zer = 0
    for i in range(1,l+1):
        zer += math.floor(n/5**i)
    return zer
    
N = int(input().strip())
 
for _ in range(N):
    n = int(input().strip())
    print(zeros(n)) 
