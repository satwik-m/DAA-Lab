def search(a,l,h):
	m=(l+h)//2
	if l>h:
		return None

	if a[m]>a[m+1] and a[m]>a[m-1]:
		return a[m]

	if a[m]>a[m+1] and a[m]<a[m-1]:
		search(a,l,m)

	if a[m]<a[m+1] and a[m]>a[m-1]:
		search(a,m,h)

def main():
	a=input('enter the sequence of numbers  ')
	a=a.split()
	for i in range(len(a)):
		a[i]=int(a[i])
	print(a)
	print('the required element is ',search(a,0,len(a)-1))


if __name__ == '__main__':
	main()