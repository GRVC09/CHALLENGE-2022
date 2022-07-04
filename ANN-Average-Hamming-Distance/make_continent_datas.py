num_per_chrom=[]
num_per_continet=[]
num_total=0
print('Making groups of coninents...')
with open('Information.txt','r') as info:			#From the Information file, we get the number of reads per chromosome and the 
	for i in range(1,5):							#number of known samples per continent
		line=info.readline()
		if i==2:
			a=line.split()
		if i==4:
			b=line.split()
for i in range(len(a)):
	num_per_chrom.append(int(a[i]))
	num_total+=int(a[i])
for i in range(len(b)):
	num_per_continet.append(int(b[i]))


continents={'EUR','AFR','AMR','SAS','EAS','UNK'}				#List of continents

sampl_per_continent={'EUR':int(num_per_continet[0]),'AMR':int(num_per_continet[1]),'SAS':int(num_per_continet[2]),							#Dictionaries between continents and how many samples have,
'EAS':int(num_per_continet[3]),'AFR':int(num_per_continet[4]),'UNK':int(num_per_continet[5])}												#continents and the *.dat where there are all the information 
																																			#for each continent, and continents with the *_set.dat file
continent_dat={'EUR':'EUR.dat','AMR':'AMR.dat','SAS':'SAS.dat', 'EAS':'EAS.dat' ,'AFR':'AFR.dat','UNK':'UNK.dat'}							#where we store only the values that we will need in the next steps

continent_set={'EUR':'EUR_set.dat','AMR':'AMR_set.dat','SAS':'SAS_set.dat', 'EAS':'EAS_set.dat' ,'AFR':'AFR_set.dat','UNK':'UNK_set.dat'}

for continent in continents:
	continent_chrom=[]
	for i in range(sampl_per_continent[continent]):
		continent_chrom.append([])

	with open(continent_dat[continent],'r') as fh:	
		ref=0
		count=0
		for line in fh:
			a=line.split()
			if 	ref==num_total:
				count+=1
				ref=0
			value=int(a[2])+int(a[3])																										#In this case, we consider that 1|1 is only 1, which that means
			if value>=1:																													#In this position, the chromosome has the REF and ALT forms in
				value=1																														#both cases, so we consider only that scenario as one
			ref+=1

	fh = open(continent_set[continent],'w')

	for i in range(0,len(continent_chrom)):
	
		for j in range(len(continent_chrom[i])):
			fh.write(str(continent_chrom[i][j]))
			fh.write('\t')
		fh.write('\n')

