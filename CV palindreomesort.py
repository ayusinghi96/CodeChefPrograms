from itertools import permutations
final,a = [],[]
s = input()
n = len(s)//2
m = len(s)%2
if m is 1:
    mid = s[n]
else:
    mid = ''
new = s[0:n]
cases = [''.join(p) for p in permutations(new)]
for i in sorted(cases):
    k = i+mid+i[::-1]
    a.append(k)
for i in a:
    if i not in final:
        final.append(i)
for i in final:
    print (i)
    

