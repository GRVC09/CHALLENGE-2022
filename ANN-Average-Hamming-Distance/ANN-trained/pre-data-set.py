import re
import os
import sys
print('Processing *.csv files.')
def read_tsv(file):
	'''Retunr datas from .tsv files in order as 
	Chrom, Pos, Ref, Alt Alt, Format1, Format2, empty '''
	file_input=[]
	with open(file,'r') as fh:
		AA=True
		for line in fh:
			if AA:
				nada=line	#Skip the first line
				AA=False
			else:						
				str = re.split(r';|,|\.|"', line)	#Split the line by ;,\. or "		
				file_input.append(str)				
	return	file_input





num_al_chrm=[0]*22
bol_to_len_chrm=True
relation_list={'EUR':[],'AMR':[],'SAS':[],'EAS':[],'AFR':[],'UNK':[]}
UNK=open('UNK.dat','w')
for x in os.listdir(os.path.dirname(os.path.abspath(sys.argv[0]))):		#Read al the  files in the current path
	if x.endswith('.csv'):												#Read .csv files		
		continent='UNK'	
		relation_list[continent].append(x)
		file_in =read_tsv(x)
		if bol_to_len_chrm:
			for j in range(len(file_in)):
				dum=file_in[j]
				num_al_chrm[int(dum[0])-1]=num_al_chrm[int(dum[0])-1]+1
			bol_to_len_chrm=False	
		for j in range(len(file_in)):
			dum=file_in[j]
			UNK.write(dum[0])									
			UNK.write('\t')			
			UNK.write(dum[1])									
			UNK.write('\t')
			UNK.write(dum[6])									
			UNK.write('\t')
			UNK.write(dum[7])									
			UNK.write('\n')


INFORMATION=open('Information.txt','w')
INFORMATION.write('#Len_per_Chromosom')
INFORMATION.write('\n')
for i in range(len(num_al_chrm)):
	INFORMATION.write(str(num_al_chrm[i]))
	INFORMATION.write('\t')
INFORMATION.write('\n')
INFORMATION.write('#Len_per_Continent	EUR	AMR	SAS	EAS	AFR	UNK')
INFORMATION.write('\n')
INFORMATION.write(str(42))
INFORMATION.write('\t')
INFORMATION.write(str(31))
INFORMATION.write('\t')
INFORMATION.write(str(40))
INFORMATION.write('\t')
INFORMATION.write(str(47))
INFORMATION.write('\t')
INFORMATION.write(str(39))
INFORMATION.write('\t')
INFORMATION.write(str(len(relation_list['UNK'])))
INFORMATION.write('\n')
INFORMATION.write('#UNK')
INFORMATION.write('\n')
for i in range(len(relation_list['UNK'])):
	INFORMATION.write(str(relation_list['UNK'][i]))
	INFORMATION.write('\t')
