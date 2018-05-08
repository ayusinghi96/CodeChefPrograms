t = int(input())
for i in range(0,t):
    n = int(input())
    a = list(input())
    b = list(input())
    if "." not in b:
        for j in range(0,n-1):
            if a[j] is "." and a[j+1] is "#":
                for m in range(j+2,n):
                    if a[m] is ".":
                        k = 0
                        break
                    else:
                        k = 1
                        break
    elif "." not in a:
        for j in range(0,n-1):
            if b[j] is "." and b[j+1] is "#":
                for m in range(j+2,n):
                    if b[m] is ".":
                        k = 0
                        break
                    else:
                        k = 1
                        break
    else:
        for j in range(0,n-1):
            if a[j+1] is "." and b[j] is "." or a[j] is "#" and b[j] is "#" and a[j+1] is "." and b[j+1] is ".":
                for m in range(j+1,n):
                    if a[m] is "#" or b[m] is "#":
                        k = 0
                        break
                    else:
                        k = 1
                break
            elif a[j] is "#" and b[j] is "#" and a[j+1] is "#" or a[j] is "#" and b[j] is "#" and b[j+1] is "#" :
                k = 0
                break
            else:
                k = 1
    if k == 1:
        print("yes")
    else:
        print("no")
        
    
        
