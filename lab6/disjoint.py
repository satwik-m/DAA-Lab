class disjoint:
	def __init__(self,n):
		self.l=[Node(i) for i in range(n)]

	def findSet(self,y):
		x=y
		while y!=y.parent:
			y=y.parent
		temp=x.parent
		while x!=y:
			x.parent=y
			x=temp
			temp=x.parent
		return y

	def union(self,x,y):
		rx=self.findSet(self.l[x])
		ry=self.findSet(self.l[y])
		if rx!=ry:
			if rx.rank>ry.rank:
				ry.parent=rx
				rx.comp+=ry.comp
				ry.comp=[]
			elif ry.rank>rx.rank:
				rx.parent=ry
				ry.comp+=rx.comp
				rx.comp=[]
			else:
				rx.parent=ry
				ry.rank+=1
				ry.comp+=rx.comp
				rx.comp=[]

	def printlist(self):
		for i in self.l:
			if len(i.comp)>1:
				print(i.comp)

class Node:
	def __init__(self,val):
		self.parent=self
		self.rank=0
		self.value=val
		self.comp=[val]

def main():
	n=int(input('enter the no. of vertices'))
	D=disjoint(n)
	e=int(input('enter the no. of edges'))
	for i in range(e):
		l=input('edge: ')
		l=l.split()
		D.union(int(l[0]),int(l[1]))
	D.findSet(D.l[3])
	rep=D.findSet(D.l[0])
	print(rep.value)
	D.printlist()

if __name__ == '__main__':
	main()

