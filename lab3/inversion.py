import math

def count_inv(A,low,high):
	if low<high:
		mid=(low+high)//2
		i1=count_inv(A,low,mid)
		#print(i1)
		i2=count_inv(A,mid+1,high)
		isp=count_split(A,low,mid,high)
		if i1==None:
			i1=0
		if i2==None:
			i2=0
		return i1+i2+isp
	return 0

def count_split(A,low,mid,high):
	l=0
	r=0
	L=[]
	R=[]
	count=0
	for i in range(low,mid+1):
		L=L+[A[i]]
	for i in range(mid+1,high+1):
		R=R+[A[i]]
	i=low
	while (l<mid-low+1) and (r<high-mid):
		if L[l]>R[r]:
			A[i]=R[r]
			r=r+1
			count+=len(L)-l
		else:
			A[i]=L[l]
			l=l+1
		i=i+1
	if l<mid-low+1:
		while l<mid-low+1:
			A[i]=L[l]
			l=l+1
			i=i+1
	else:
		while r<high-mid:
			A[i]=R[r]
			r=r+1
			i=i+1
	return count

#l=int(input('enter the sequence '))
#l=l.split()
print('No. of inversions = ',count_inv([4,10,8,2,1],0,4))