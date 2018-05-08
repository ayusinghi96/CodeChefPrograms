def coordinate(m,n,a,b):
    l= a-m
    k= b-n
    if(l > 0):
        for i in range(a,n1):
            if p[i][b] is 1:
                count + = 1
                coordinate(a,b,i,b)
                break
        for j in range(b,n1):
            if p[a][j] is 1:
                count +=1
                coordinate(a,b,a,j)
                break
        for j in range(b,O,-1):
            if p[a][j] is 1:
                count +=1
                coordinate(a,b,a,j)
                break
    elif(l < 0):
        for i in range(a,0,-1):
            if p[i][b] is 1:
                count +=1
                coordinate(a,b,i,b)
                break
        for j in range(b,n1):
            if p[a][j] is 1:
                count +=1
                coordinate(a,b,a,j)
                break
        for j in range(b,O,-1):
            if p[a][j] is 1:
                count +=1
                coordinate(a,b,a,j)
                break
    elif(k > 0):
        for i in range(a,n1):
            if p[i][b] is 1:
                count +=1
                coordinate(a,b,i,b)
                break
        for i in range(a,0,-1):
            if p[i][b] is 1:
                count +=1
                coordinate(a,b,i,b)
                break
        for j in range(b,n1):
            if p[a][j] is 1:
                count +=1
                coordinate(a,b,a,j)
                break
    else:
        for i in range(a,n1):
            if p[i][b] is 1:
                count +=1
                coordinate(a,b,i,b)
                break
        for i in range(a,0,-1):
            if p[i][b] is 1:
                count +=1
                coordinate(a,b,i,b)
                break
        for j in range(b,O,-1):
            if p[a][j] is 1:
                count +=1
                coordinate(a,b,a,j)
                break





    
n1 = int(input())
p,q = [],[]

for i in range(0,n1):
    p.append(list(map(int,input().split(','))))
m,n = input().split(',')
x,y = input().split(',')
for i in range(m,n1):
    if p[i][n] is 1:
        q.append([i,n])
        break
for i in range(m,0,-1):
    if p[i][n] is 1:
        q.append([i,n])
        break
for i in range(n,n1):
    if p[m][i] is 1:
        q.qppend([m,i])
        break
for i in range(n,0,-1):
    if p[m][i] is 1:
        q.append([m,i])
while x in q:
    coordinate(

    

