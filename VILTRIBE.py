t = int(input())
for i in range(t):
    a = input()
    count_a,count_b = a.count('A'), a.count('B')
    for z in range(a):
        if a[z] == '.':
            b = a.index('.')
            for k in range(len(a)-b):
                if a[k] == 'A':
                    for j in range(b,0,-1):
                        if a[j] == 'A':
                            count_a += 1
                            break
                if a[k] == 'B':
                    for j in range(b,0,-1):
                        if a[j] == 'B':
                            count_b += 1
                            break
        
                
    print(str(count_a)+' '+str(count_b))
