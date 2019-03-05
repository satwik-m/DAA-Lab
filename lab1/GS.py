def main():
	f=open("input.txt","r")

	men=f.readline()
	men=men.split()
	n=len(men)
	women=f.readline()
	women=women.split()
	mendict={}
	womendict={}

	for i in range(n):
		mendict[men[i]]=i
		womendict[women[i]]=i

	#print(womendict)
	freemen=[i for i in range(n)]
	freewomen=[i for i in range(n)]

	wife=[None]*n
	husband=[None]*n

	mpref=[[None for i in range(n)]for j in range(n)]
	wpref=[[None for i in range(n)]for j in range(n)]
	w1pref=[[None for i in range(n)]for j in range(n)]
	mprop=[0]*n
	for i in range(n):
		pref=f.readline()
		pref=pref.split()
		for j in range(n):
			mpref[mendict[pref[0]]][j]=womendict[pref[j+1]]
			

	for i in range(n):
		pref=f.readline()
		pref=pref.split()
		for j in range(n):
			wpref[womendict[pref[0]]][j]=mendict[pref[j+1]]

	for i in range(n):
		for j in range(n):
			w1pref[i][wpref[i][j]]=j

	#for i in range(2):
	#	print(mpref[i])
	#	print(wpref[i])

	while len(freemen)>0:
		m=freemen[0]
		while mprop[m]<n:
			w=mpref[m][mprop[m]]
			#print(w)
			if husband[w]==None:
				husband[w]=m
				freemen=freemen[1:]
				mprop[m]+=1
				break
				
			elif w1pref[w][m]<w1pref[w][husband[w]]:
				freed=husband[w]
				husband[w]=m
				freemen=freemen[1:]
				freemen+=[freed]
				mprop[m]+=1
				break
			else:
				mprop[m]+=1

	for i in range(n):
		print(men[husband[i]],'-',women[i])

if __name__ == '__main__':
	main()



			

	
