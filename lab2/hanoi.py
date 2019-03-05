def solvehanoi(n,s,i,t):
	if n>1:
		solvehanoi(n-1,s,t,i)
		print('Move Disk ',n,' from peg ',s,' to ',t)
		solvehanoi(n-1,i,s,t)

	if n==1:
		print('Move Disk ',n,' from peg ',s,' to ',t)

def main():
	n=int(input("enter the no. of disks "))
	solvehanoi(n,'s','i','t')

if __name__ == '__main__':
	main()