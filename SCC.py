class dag:
	def __init__(self,n):
		self.adj=[node(i) for i in range(n)]
		self.revadj=[node(i) for i in range(n)]
		self.l=[i for i in range(n)]
		self.time=0
		self.l=[i for i in range(n)]

	def insert(self,a,b):
		self.adj[a].edge+=[b]
		self.revadj[b].edge+=[a]

	def revdfs(self,u):
		self.revadj[u].start=self.time
		self.time+=1
		self.revadj[u].color='grey'
		self.l.remove(u)
		for i in self.revadj[u].edge:
			if self.revadj[u].color=='white':
				self.revdfs(i)
				self.revadj[i].pred=u
		self.revadj[u].color='black'
		self.revadj[u].end=self.time
		self.time+=1

	def dfs(self,u):
		#self.revadj[u].start=self.time
		#self.time+=1
		print(u,end=' ')
		self.l.remove(u)
		self.adj[u].color='grey'
		for i in self.adj[u].edge:
			if self.adj[i].color=='white':
				self.dfs(i)
				self.adj[i].pred=u
		self.adj[u].color='black'
		#self.adj[u].end=self.time
		#self.time+=1

class node:
	def __init__(self,v):
		self.v=v
		self.start=None
		self.end=None
		self.color='white'
		self.edge=[]
		self.pred=None

def main():
	n=int(input('enter no. of vertices '))
	e=int(input('enter no. of edges '))
	g=dag(n)
	print('enter the edges')
	for i in range(e):
		l=input()
		l=l.split()
		g.insert(int(l[0]),int(l[1]))
	
	while(len(g.l)>0):
		g.revdfs(g.l[0])
	g.l=[i for i in range(n)]
	for i in range(n-1):
		for j in range(n-i-1):
			if g.revadj[g.l[j]].end<g.revadj[g.l[j+1]].end:
				t=g.l[j]
				g.l[j]=g.l[j+1]
				g.l[j+1]=t

	print('strongly connected components are')
	while(len(g.l)>0):
		g.dfs(g.l[0])
		print('')

main()



