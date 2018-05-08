t = int(input())
a=[]
s=0
for i in range(0,t):
    n = int(input())
    a = list(map(int,input().split(' ')))
    ##print(a)
    for j in range(0,int(n/2)):
        if(a[j] <= 7):
            if(a[j+1] == a[j]+1 or a[j+1] == a[j]):
                if (a[j] == a[n-j-1]):
                    a.pop()
                    s += 1
                else:
                    print("no")
                    break
            else:
                print("no")
                break
        else:
            print("no")
            break
    if(s == int(n/2)):
        print("yes")
