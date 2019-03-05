
def sortt(x):
	return x[1]

def function(T):
	t=T[0][1]
	print(T[0])
	for i in T:
		if i[0]>t:
			t=i[1]
			print(i)


n=int(input('enter the number of intervals  '))
T=[[] for i in range(n)]
print('enter the intervals')
for i in range(n):
	l=input()
	l=l.split()
	T[i]=[int(l[0]),int(l[1])]

T.sort(key=sortt)
function(T)

