from itertools import permutations
si = raw_input()
if len(si)%2 is 1:
        c=si[len(si)/2]
else:
        c = ''
s=si[0:len(si)/2]
s1=[''.join(p) for p in permutations(s)]
s1=list(set(s1))
s1.sort
for i in s1:
	print i+c+i[::-1]
