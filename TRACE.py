def Trace(mat):
    trace = 0
    maxTrace = trace
    k = 0
    for k in range(2,n-k):
        if k>n:
            return
        for i in range(n-k+1):
            for j in range(n-k+1):
                trace = 0
                ctr = 0
                for p in range(i,k+i):
                    trace += mat[i+ctr][j+ctr]
                    ctr += 1
                if maxTrace < trace:
                    maxTrace = trace
    return maxTrace
                

global n
t = int(input())
mat = []
for i in range(t):
    n = int(input())
    for j in range(n):
        mat.append(list(map(int,input().split(" "))))
    print(Trace(mat))
    
