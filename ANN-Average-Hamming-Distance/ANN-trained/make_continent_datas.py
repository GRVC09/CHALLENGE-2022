num_per_chrom=[]
num_per_continet=[]
num_total=0
with open('Information.txt','r') as info:
	for i in range(1,5):
		line=info.readline()
		if i==2:
			a=line.split()
		if i==4:
			b=line.split()
for i in range(len(a)):
	num_per_chrom.append(int(a[i]))
	num_total+=int(a[i])
print(num_per_chrom)
for i in range(len(b)):
	num_per_continet.append(int(b[i]))
print(num_per_continet)

continents={'UNK'}

sampl_per_continent={'EUR':int(num_per_continet[0]),'AMR':int(num_per_continet[1]),'SAS':int(num_per_continet[2]),
'EAS':int(num_per_continet[3]),'AFR':int(num_per_continet[4]),'UNK':int(num_per_continet[5])}

continent_dat={'UNK':'UNK.dat'}

continent_set={'UNK':'UNK_set.dat'}

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

