t = int(input())
if t >= 1 and t <= 10:
    for i in range(0,t):
        a = []
        p = []
        m = 0
        n,k = map(int,input().split())                            
        for i in range(0,n):
            a.append(list(map(int,input().split())))
            p.extend(a[i][1:])
        for i in range(1,k+1):
            if i not in p:
                m += 1
                break
        if m == 1:
            print ("sad")
        else:
            for g in range(1,n+1):
                z = []
                m = 0
                for j in range(0,g):
                    for x in range(1,k+1):
                        if x in a[j][1:]:
                            z.append(x)
                    for y in range(1,k+1):
                        if y in z:
                            m += 1
                    if m == k:
                        print ("some")
                        break
                if m == k:
                    break
            if g == n:
                print ("all")
            
        
                
        
            
            
