import heapq
class BinaryHeap:
	def __init__(self,L):
		self.E=[None]+L
		self.l=len(self.E)
		self.BuildHeap()

	def heapify(self,i):
		if (i<=(self.l-1)/2) and (i>0):
			if(2*i+1<self.l):
				t2=self.E[2*i+1].freq
			t1=self.E[2*i].freq
			if (2*i+1<self.l) and (self.E[i].freq>t2) and (t1>t2):
				t=self.E[2*i+1]
				self.E[2*i+1]=self.E[i]
				self.E[i]=t
				k=i*2+1
			elif(self.E[i].freq>t1):
				t=self.E[2*i]
				self.E[2*i]=self.E[i]
				self.E[i]=t
				k=2*i
			else:
				k=-1
			self.heapify(k)


	def BuildHeap(self):
		for i in range(int((self.l-1)/2),0,-1):
			self.heapify(i)


	def extractMin(self):
		t=self.E[1]
		self.E[1]=self.E[self.l-1]
		self.E[self.l-1]=t
		t=self.E[self.l-1]
		del self.E[self.l-1]
		self.l-=1
		self.heapify(1)
		return t

	def insert(self,k):
		self.l+=1
		self.E.append(k)
		i=int((self.l-1)/2)
		while i>0:
			self.heapify(i)
			i=int(i/2)

class Node:
	def __init__(self):
		self.freq=None
		self.key=None
		self.left=None
		self.right=None
		self.code=''

class huffman:
	def __init__(self,s,f):
		self.l=[]
		self.root=None
		for i in range(len(s)):
			n=Node()
			n.key=s[i]
			n.freq=f[i]
			self.l+=[n]
		self.H=BinaryHeap(self.l)

	def tree_formation(self):
		for i in range(len(self.l)-1):
			n=Node()
			n1=self.H.extractMin()
			n2=self.H.extractMin()
			n.left=n1
			n.right=n2
			n.freq=n1.freq+n2.freq
			self.H.insert(n)
		self.root=self.H.extractMin()

	def makeCodes(self,n,str):
		if n.key!=None:
			n.code=str
			return
		self.makeCodes(n.left,str+'0')
		self.makeCodes(n.right,str+'1')


def main():
	s=['a','b','f','z']
	f=[3,6,2,4]
	h=huffman(s,f)
	h.tree_formation()
	h.makeCodes(h.root,'')
	print('codes are')
	for i in h.l:
		print(i.key,'-',i.code)
	

if __name__ == '__main__':
	main()