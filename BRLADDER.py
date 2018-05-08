##bear and ladder
##There are roads 1-2, 3-4, 5-6, 7-8, and so on (there is a road between cities 2*i+1 and 2*i+2 for every non-negative integer i).
##There are roads 1-3, 3-5, 5-7, 7-9, ... (between every two consecutive odd numbers).
##There are roads 2-4, 4-6, 6-8, 8-10, ... (between every two consecutive even numbers).
q = int(input())
if q<=1000 and q>=1 :
    a = []
    for i in range(0,q):
        a.append(list(map(int,input().split())))
    print (a)
    for i in range(0,q):
        ## when input is even
        if a[i][0]%2==0:
            if a[i][1]==a[i][0]-1 or a[i][1]==a[i][0]+2 or a[i][1]==a[i][0]-2:
                print("YES")
            else:
                print("NO")
        ## when input is odd
        else:
            if a[i][1]==a[i][0]+1 or a[i][1]==a[i][0]+2 or a[i][1]==a[i][0]-2:
                 print("YES")
            else:
                print("NO")
            
