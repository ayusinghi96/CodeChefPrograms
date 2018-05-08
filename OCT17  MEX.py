t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    s = list(map(int,input().split()))
    m = set(s)
    if k != 0:
        totallist = set(list(range(max(s)+ k + 5)))
##        print("totallist", totallist)
        new_set = totallist - m
##        print(new_set)
        final_list = list(new_set)
        print(final_list[k])
        
    else:
        totallist = set(list(range(max(s)+ 3)))
##        print("totallist", totallist)
        new_set = totallist - m
##        print(new_set)
        final_list = list(new_set)
        print(final_list[k])
        
    
    
