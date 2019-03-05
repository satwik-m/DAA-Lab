class node:
	def __init__(self,val,weight):
		self.val=val
		self.weight=weight

def floyd_warshall(D,P):
	for k in range(1,n+1):
		D[k]=[[None for i in range(n+1)] for j in range(n+1)]
		for i in range(1,n+1):
			for j in range(1,n+1):
				D[k][i][j]=min(D[k-1][i][j],D[k-1][i][k]+D[k-1][k][j])
				m=D[k][i][j]
				if m==D[k-1][i][j]:
					P[k][i][j]=P[k-1][i][j]
				else:
					P[k][i][j]=P[k-1][k][j]
	return D[n]

def printpath(a,b,P,l):
	if a==b:
		return l
	else:
		print(P[a][b])
		l=[P[a][b]]+l
		printpath(a,P[a][b],P,l)


n=int(input('enter the no. of vertices  '))
e=int(input('enter the no. of edges  '))
print('enter the edges and weights')
adj=[[None for i in range(n+1)] for j in range(n+1)]
D=[None for i in range(n+1)]
P=[None for i in range(n+1)]
D[0]=[[None for i in range(n+1)] for j in range(n+1)]
P[0]=[[None for i in range(n+1)] for j in range(n+1)]
for i in range(e):
	s=input()
	s=s.split()
	x=node(int(s[1]),int(s[2]))
	adj[int(s[0])][int(s[1])]=x
for i in range(1,n+1):
	for j in range(1,n+1):
		if i==j:
			D[0][i][j]=0
		elif adj[i][j]!=None:
			D[0][i][j]=adj[i][j].weight
			P[0][i][j]=i
		else:
			D[0][i][j]=float('inf')

for i in range(1,n+1):
	P[i]=[[None for i in range(n+1)] for j in range(n+1)]
a=floyd_warshall(D,P)
p=printpath(1,2,P[n],[])
print(p)


