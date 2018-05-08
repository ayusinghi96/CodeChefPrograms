t = int(input())
for i in range(0,t):
      n = int(input())
      a = list(map(int,input().split()))
      c = 0
      if(0 in a):
            d = a.index(0)
            for j in range(d,n):
                  if(a[j]==0):
                        c += 1100
                  else:
                        c += 100
      print(c)
