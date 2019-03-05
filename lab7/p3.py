
def sortt(x):
	return x[1]

def function(T,n):
	r=0
	rmin=n
	m=T[-1][1]+1
	while len(T)!=0:
		t=T[0][1]
		print(T[0],end=' ')
		i=0
		l=len(T)
		while i<l:
			if T[i][0]>t:
				t=T[i][1]
				print(T[i],end=' ')
				r=r+1
				if r<rmin:
					rmin=r
				T.remove(T[i])
				i=i-1
		print()


n=int(input('enter the number of intervals  '))
T=[[] for i in range(n)]
print('enter the intervals')
for i in range(n):
	l=input()
	l=l.split()
	T[i]=[int(l[0]),int(l[1])]

T.sort(key=sortt)
function(T,n)

