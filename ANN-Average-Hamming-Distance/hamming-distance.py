'''
This algorithm returns the *ham.dat and *avr.dat files that result from the normalized 
Hamming distance concerning the data sets that we know where they are from. We have 
five Hamming distances for each sample (EUR,AMR,SAS,EAS,AFR). *.ham gives us the average 
Hamming distance divided by each chromosome, while *.avr is the total average Hamming 
distance. So *.ham has (22*5)=110 columns, and *.avr has only 5.

'''
list_chrom=[5,1,15,17,9,2,8,14,12,4,13,3,19,11,10,7,18,6,16,21,20,22]	#Chromosome positioning list in .vcf files.
num_per_chrom=[]
num_per_continet=[]
num_total=0
with open('Information.txt','r') as info:				#Open the information
	for i in range(1,5):
		line=info.readline()
		if i==2:						#number of reads per chromosome
			a=line.split()
		if i==4:
			b=line.split()					#number of samples per continent
total_all=0
for i in range(len(a)):
	num_per_chrom.append(int(a[i]))
	num_total+=int(a[i])
	total_all+=int(a[i])
print(num_per_chrom)							#List of number of reads per chromosome
for i in range(len(b)):
	num_per_continet.append(int(b[i]))				#List of number of samples per continent
print(num_per_continet)	

def hamming_distance(line_ref,line_search):
	'''
	This function compute the Hamming distance from lines in *set.dat files.
	The Hamming distance is compute for any chromosome (chrm) and by the average 
	over the complete genotype. 
	'''
	chrm=[]
	for i in range(22):
		chrm.append([])
	ref=[]
	search=[]
	for i in range(len(line_ref)):
		ref.append(int(line_ref[i]))
		search.append(int(line_search[i]))
	n=0
	i=0
	m=0
	match=0
	total_match=0
	while i < len(list_chrom):
		limit=num_per_chrom[list_chrom[i]-1]
		if n==limit:
			hamming_chrom=float(match)/limit			#Divide the Hamming distance for any chromosome
			chrm[list_chrom[i]-1].append(hamming_chrom)
			match=0
			i+=1
			n=0
		if i==22:
			break
		if ref[m]==search[m]:						#If we have two equal reads at the same position, we have a match
			match+=1						#For example, if the FORM in a vcf file is 0|1 and in other sample es 1|0
			total_match+=1						#we have a match, the same for 1|1->0|1 1|0, 0|0->0|0, and so on.
		else:								#Mismatch occurs when two samples are not equal even in the ALT form 0|1->0|0
			match+=0
			total_match+=0

		m+=1
		n+=1
	hamming_avarage=float(total_match)/total_all				#Hamming distance average between the reference genotype (line_ref) and the search genotype (line_search)
	return chrm,hamming_avarage

continents={0:'EUR',1:'AMR',2:'SAS',3:'EAS',4:'AFR'}																		#Dictionary of known sets
sampl_per_continent={'EUR':int(num_per_continet[0]),'AMR':int(num_per_continet[1]),'SAS':int(num_per_continet[2]),
'EAS':int(num_per_continet[3]),'AFR':int(num_per_continet[4]),'UNK':int(num_per_continet[5])}					#Dictionary of known sets and how many samples each one has

continent_hamming={'EUR':'EUR_ham.dat','AMR':'AMR_ham.dat','SAS':'SAS_ham.dat', 'EAS':'EAS_ham.dat' ,'AFR':'AFR_ham.dat'}	#Dictionaries of known sets and the outputs files.
continent_avr={'EUR':'EUR_avr.dat','AMR':'AMR_avr.dat','SAS':'SAS_avr.dat', 'EAS':'EAS_avr.dat' ,'AFR':'AFR_avr.dat'}

EUR=[]
ref=open('EUR_set.dat','r')
for i in range(sampl_per_continent['EUR']):		#Read the *set.dat files for each known continent and appent to a list
	a=ref.readline()
	EUR.append(a.split())
AMR=[]
ref=open('AMR_set.dat','r')
for i in range(sampl_per_continent['AMR']):
	a=ref.readline()
	AMR.append(a.split())
SAS=[]
ref=open('SAS_set.dat','r')
for i in range(sampl_per_continent['SAS']):
	a=ref.readline()
	SAS.append(a.split())
EAS=[]
ref=open('EAS_set.dat','r')
for i in range(sampl_per_continent['EAS']):
	a=ref.readline()
	EAS.append(a.split())
AFR=[]
ref=open('AFR_set.dat','r')
for i in range(sampl_per_continent['AFR']):
	a=ref.readline()
	AFR.append(a.split())

ALL_list=[EUR,AMR,SAS,EAS,AFR]									#List of continents

for i in range(len(ALL_list)):									#Double loop to take the Hamilton distance 3 
	chrom_ham=open(continent_hamming[continents[i]],'w')					#for each sample concerning the samples from 
	prom_ham=open(continent_avr[continents[i]],'w')						#which we know which continent they come from.
	for j in range(len(ALL_list[i])):
		ref=ALL_list[i][j]		
		for k in range(len(ALL_list)):
			n=0
			hamming_result=[0]*22
			hamming_avr=0
			for l in range(len(ALL_list[k])):
				search=ALL_list[k][l]
				if i==k:
					if j==l:						#We skip compares a sample with itself
						continue
				n+=1
				print(i,k,j,l)
				hamming_chrom,hamming_avarage=hamming_distance(ref,search)	#Call the hamming_distance function
				for m in range(22):
					hamming_result[m]+=float(hamming_chrom[m][0])
				hamming_avr+=hamming_avarage
			prom_ham.write(str(hamming_avr/n))
			prom_ham.write('\t')
			for m in range(22):
				chrom_ham.write(str(hamming_result[m]/n))			#Store the results
				chrom_ham.write('\t')
		prom_ham.write('\n')
		chrom_ham.write('\n')

UNK=[]												#Repeat the same above for the unkown reference values
ref=open('UNK_set.dat','r')
for i in range(sampl_per_continent['UNK']):
	a=ref.readline()
	UNK.append(a.split())
chrom_ham=open('UNK_ham.dat','w')
prom_ham=open('UNK_avr.dat','w')

for j in range(len(UNK)):
	ref=UNK[j]		
	for k in range(len(ALL_list)):
		n=0
		hamming_result=[0]*22
		hamming_avr=0
		for l in range(len(ALL_list[k])):
			search=ALL_list[k][l]
			n+=1
			print(j,k,l)
			hamming_chrom,hamming_avarage=hamming_distance(ref,search)
			for m in range(22):
				hamming_result[m]+=float(hamming_chrom[m][0])
			hamming_avr+=hamming_avarage
		prom_ham.write(str(hamming_avr/n))
		prom_ham.write('\t')
		for m in range(22):
			chrom_ham.write(str(hamming_result[m]/n))
			chrom_ham.write('\t')
	prom_ham.write('\n')
	chrom_ham.write('\n')
