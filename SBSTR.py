for _ in range(int(input())):
    a,k = input().split()
    n = len(a)
    k = int(k)
    ans = 0
    for i in range(n):
        b = [0]*123
        s = []
        for j in range(i,n):
            if b[ord(a[j])] == 0:
                s.append(a[j])
                b[ord(a[j])] += 1
                length = len(s)
                if length >= k:
                    m = b[ord(s[0])]
                    im = 0
                    for k in s:
                        if b[ord(k)] != m:
                            im += 1
                            break
                        if im == 0:
                            ans += 1
    print(ans)
