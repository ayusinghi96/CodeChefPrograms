  ##  Input
  ##  The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.

  ##  The first line of each test case contains an integer N denoting the number of minutes.

  ##  The second line of a test case contains N space-separated strings S1, S2, ..., SN. The string Si is either "cookie" (if Limak eats a cookie in the i-th minute) or "milk" (otherwise).

  ##  Output
  ##  For each test case, output a single line containing the answer — "YES" if Limak followed his parents' instructions, and "NO" otherwise, both without the quotes.

  ##  Constraints
  ##  1 ≤ T ≤ 50
  ##  1 ≤ N ≤ 50
  ##  Each Si is either "cookie" or "milk" (without the quotes).
  ##  Subtasks
  ##  Subtask #1 (40 points) N = 2
  ##  Subtask #2 (60 points) Original constraints
  ##  Example
  ##  Input:
  ##  4
  ##  7
  ##  cookie milk milk cookie milk cookie milk
  ##  5
  ##  cookie cookie milk milk milk
  ##  4
  ##  milk milk milk milk
  ##  1
  ##  cookie

  ##  Output:
  ##  YES
  ##  NO
  ##  YES
  ##  NO


t=int(input())
a = []
l = []
if 1 <= t and t <= 50:
    for i in range(0,t):
        l.append(int(input()))
        a.append(input().split())
    if max(l) <= 50 and min (l) >= 1:
        for i in range(0,t):
            n = 0
            m = l[i]
            x = a[i]
            for j in range(0,m):
                if x[j] == 'milk' or x[j] =='cookie':
                    n += 1
                else:
                    exit()
            if n == m:
                n = 0
                ## taking the inputs in which cookie is at last place or the only input is cookie
                if x[m-1] == 'cookie':
                    print ("NO")
                else:
                ## checking for every other place
                    for j in range(0,m-1):
                        if x[j] == 'cookie' and x[j+1] == 'cookie':
                            print ("NO")
                            break
                        else:
                            n += 1
                    if n > 0:
                        print ("YES")
                           
                       
        
        
        
    

