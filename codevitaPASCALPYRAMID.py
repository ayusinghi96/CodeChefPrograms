def fun():
	n = int(input())
	p = list(map(int,input().split(',')))
	p.sort()
	a = p[(n-6):n]
	b = [a[1],a[3],a[4],a[5],a[2],a[0]]
	for j in range(0,4):
	    for i in range(0,5-j):
	        b[i]=(b[i]+b[i+1])
	    b.pop()
	print(b[0]*b[1])
if __name__ =="__main__":
	fun()
