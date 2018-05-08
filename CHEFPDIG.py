from itertools import combinations,permutations,product
t = int(input())
for t in range(0,t):
    a = []
    n = input()
    if '6' in n:
        b = n[:n.index('6')] + n[n.index('6')+1:]
        for i in range(5,10):
            if str(i) in b:
                a.append(int('6' + str(i)))


                
    for j in range(7,10):
        if str(j) in n:
            b = n[:n.index(str(j))] + n[n.index(str(j))+1:]
            for i in range(0,10):
                if str(i) in b:
                    a.append(int(str(j) + str(i)))
    if len(a) is 0:
        print()
    else:
        for i in range(0,len(a)):
            if a[i] >= 65 and a[i] <= 90:
                print(chr(a[i]),end = '')
        print()
    
            
            
        
    
