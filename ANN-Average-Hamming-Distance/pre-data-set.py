import re
import os
import sys

def read_coordi(file):
	#This function read the coordination.txt to get the known files
	file_input=[]
	with open(file,'r') as fh:
		AA=True
		for line in fh:
			if AA:
				nada=line					#Skip the first line
				AA=False
			else:						
				file_in = line.split()		#Split the line in the file_name,Continent
				file_input.append(file_in)	#Fill the searching list with known files
	return	file_input

def read_tsv(file):
	'''Retunr datas from .tsv files in order as 
	Chrom, Pos, Ref, Alt Alt, Format1, Format2, empty '''
	file_input=[]
	with open(file,'r') as fh:
		AA=True
		for line in fh:
			if AA:
				nonth=line	#Skip the first line
				AA=False
			else:						
				str = re.split(r';|,|\.|"', line)	#Split the line by ;,\. or "		
				file_input.append(str)				
	return	file_input


file_input =read_coordi('coordination.txt')			#Read the known files

EUR=open('EUR.dat','w')
AMR=open('AMR.dat','w') 
SAS=open('SAS.dat','w') 
EAS=open('EAS.dat','w') 
AFR=open('AFR.dat','w')
UNK=open('UNK.dat','w') 


known_set=[]
for i in range(len(file_input)):
	a=file_input[i]
	a[0]+='.csv'									#Read the .csv file from a known files 
	known_set.append(a)								#Save the continent in known_set list



num_al_chrm=[0]*22
bol_to_len_chrm=True
relation_list={'EUR':[],'AMR':[],'SAS':[],'EAS':[],'AFR':[],'UNK':[]}

for x in os.listdir(os.path.dirname(os.path.abspath(sys.argv[0]))):		#Read al the  files in the current path
	if x.endswith('.csv'):							#Read only *.csv files
		
		for i in range(len(known_set)):			
			if x==known_set[i][0]:
				continent=known_set[i][1]			#Recognize if we know the continent, otherwise we will call it UNK.
				break
			else:
				continent='UNK'	
		relation_list[continent].append(x)
		file_in =read_tsv(x)
		if bol_to_len_chrm:
			for j in range(len(file_in)):
				dum=file_in[j]
				num_al_chrm[int(dum[0])-1]=num_al_chrm[int(dum[0])-1]+1	#Count how many read are per chromosome
			bol_to_len_chrm=False
		if continent=='EUR':
			q=EUR
		if continent=='AMR':
			q=AMR
		if continent=='SAS':
			q=SAS
		if continent=='EAS':
			q=EAS
		if continent=='AFR':
			q=AFR
		if continent=='UNK':
			q=UNK
	
		for j in range(len(file_in)):					#Write all the values in the same file as its continent name: EUR-->EUR.dat
			dum=file_in[j]						#If the sample doesn't have any reference then store UNK-->UNK.dat
			q.write(dum[0])									
			q.write('\t')			
			q.write(dum[1])									
			q.write('\t')
			q.write(dum[6])									
			q.write('\t')
			q.write(dum[7])									
			q.write('\n')


INFORMATION=open('Information.txt','w')						#Write all the information from the genotypes in the Information.txt
INFORMATION.write('#Len_per_Chromosom')						#Number of reads per chromosome, number of samples per continent
INFORMATION.write('\n')								#And the names of the files for each continent
for i in range(len(num_al_chrm)):
	INFORMATION.write(str(num_al_chrm[i]))
	INFORMATION.write('\t')
INFORMATION.write('\n')
INFORMATION.write('#Len_per_Continent	EUR	AMR	SAS	EAS	AFR	UNK')
INFORMATION.write('\n')
INFORMATION.write(str(len(relation_list['EUR'])))
INFORMATION.write('\t')
INFORMATION.write(str(len(relation_list['AMR'])))
INFORMATION.write('\t')
INFORMATION.write(str(len(relation_list['SAS'])))
INFORMATION.write('\t')
INFORMATION.write(str(len(relation_list['EAS'])))
INFORMATION.write('\t')
INFORMATION.write(str(len(relation_list['AFR'])))
INFORMATION.write('\t')
INFORMATION.write(str(len(relation_list['UNK'])))
INFORMATION.write('\n')
INFORMATION.write('#EUR')
INFORMATION.write('\n')
for i in range(len(relation_list['EUR'])):
	INFORMATION.write(str(relation_list['EUR'][i]))
	INFORMATION.write('\t')
INFORMATION.write('\n')
INFORMATION.write('#AMR')
INFORMATION.write('\n')
for i in range(len(relation_list['AMR'])):
	INFORMATION.write(str(relation_list['AMR'][i]))
	INFORMATION.write('\t')
INFORMATION.write('\n')
INFORMATION.write('#SAS')
INFORMATION.write('\n')
for i in range(len(relation_list['SAS'])):
	INFORMATION.write(str(relation_list['SAS'][i]))
	INFORMATION.write('\t')
INFORMATION.write('\n')
INFORMATION.write('#EAS')
INFORMATION.write('\n')
for i in range(len(relation_list['EAS'])):
	INFORMATION.write(str(relation_list['EAS'][i]))
	INFORMATION.write('\t')
INFORMATION.write('\n')
INFORMATION.write('#AFR')
INFORMATION.write('\n')
for i in range(len(relation_list['AFR'])):
	INFORMATION.write(str(relation_list['AFR'][i]))
	INFORMATION.write('\t')
INFORMATION.write('\n')
INFORMATION.write('#UNK')
INFORMATION.write('\n')
for i in range(len(relation_list['UNK'])):
	INFORMATION.write(str(relation_list['UNK'][i]))
	INFORMATION.write('\t')
