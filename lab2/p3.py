def inversion(l):
	count=0
	for i in range(len(l)):
		for j in range(i+1,len(l)):
			if l[i]>l[j]:
				temp=l[i]
				l[i]=l[j]
				l[j]=temp
				count+=1
	return count


def main():
	l=input('enter the sequence ')
	l=l.split()
	for i in range(len(l)):
		l[i]=int(l[i])
	print('the no. of inversions required is ',inversion(l))

if __name__ == '__main__':
	main()