def edit_distance(str1,str2,n,m):
	dp_array =[[0 for i in range(m)] for k in range(n)]
	for i in range(n):
		for k in range(m):
			if i==0:
				dp_array[i][k] = k
			elif k==0 :
				dp_array[i][k] = i
			if str1[i] ==str2[k]:
				dp_array[i][k] = dp_array[i-1][k-1]
			else:
				dp_array[i][k] = 1+ min(dp_array[i][k-1],dp_array[i-1][k],dp_array[i-1][k-1])

	print(dp_array[n-1][m-1])

def main():
	str1 = "hello"
	str2 = "heeeee"
	
	edit_distance(str1,str2,len(str1),len(str2))
main()