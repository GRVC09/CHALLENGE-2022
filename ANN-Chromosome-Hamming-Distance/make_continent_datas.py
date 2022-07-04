'''
This algorithm takes the data separated by continent and writes in each line of *_set.dat the information for a single sample.
'''
num_per_chrom=[]
num_per_continet=[]
num_total=0
with open('Information.txt','r') as info:			#Read how many alleles are per chromosome and how many samples are per continent
	for i in range(1,5):
		line=info.readline()
		if i==2:
			a=line.split()
		if i==4:
			b=line.split()
for i in range(len(a)):
	num_per_chrom.append(int(a[i]))				#Number of alleles per chromosome
	num_total+=int(a[i])
print(num_per_chrom)
for i in range(len(b)):
	num_per_continet.append(int(b[i]))			#Number of samples per continent
print(num_per_continet)
print('Making groups of continents')
continents={'EUR','AFR','AMR','SAS','EAS','UNK'}

sampl_per_continent={'EUR':int(num_per_continet[0]),'AMR':int(num_per_continet[1]),'SAS':int(num_per_continet[2]),	#Dictionary of continent and samples
'EAS':int(num_per_continet[3]),'AFR':int(num_per_continet[4]),'UNK':int(num_per_continet[5])}

continent_dat={'EUR':'EUR.dat','AMR':'AMR.dat','SAS':'SAS.dat', 'EAS':'EAS.dat' ,'AFR':'AFR.dat','UNK':'UNK.dat'}	#Dictionaries of read / write files 

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
			value=int(a[2])+int(a[3])
			if value>=1:
				value=1
			continent_chrom[count].append(value)
			ref+=1

	fh = open(continent_set[continent],'w')

	for i in range(0,len(continent_chrom)):
	
		for j in range(len(continent_chrom[i])):
			fh.write(str(continent_chrom[i][j]))
			fh.write('\t')
		fh.write('\n')


