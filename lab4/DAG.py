class Node:
	def __init__(self):
		self.v=None
		self.l=[]
		self.inc_edge=0

class Graph:
	def __init__(self,n):
		self.AdjList=[Node() for i in range(n)]

	def inc_edge(self):
		for i in range(len(self.AdjList)):
			for j in self.AdjList[i].l:
				self.AdjList[j].inc_edge+=1

	def traverse(self):
		s=[]
		tl1=[]
		tl2=[]
		for i in range(len(self.AdjList)):
			if self.AdjList[i].inc_edge==0:
				s+=[i]

		count=0
		while len(s)!=0:
			while len(s)!=0:
				tl2+=self.AdjList[s[0]].l
				s=s[1:]
				for j in tl2:
					self.AdjList[j].inc_edge-=1
					if self.AdjList[j].inc_edge==0:
						tl1+=[j]
				tl2=[]
			count+=1	
			s=tl1
			tl1=[]
		print(count)

def main():
	G=Graph(6)
	G.AdjList[0].l=[2]
	G.AdjList[1].l=[3]
	G.AdjList[2].l=[4,5]
	G.AdjList[3].l=[5]
	G.AdjList[4].l=[]
	G.AdjList[5].l=[4]
	G.inc_edge()
	G.traverse()

if __name__ == '__main__':
	main()
































































































































































































































































































































































































































































