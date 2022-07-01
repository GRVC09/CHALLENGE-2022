import os
import sys

for x in os.listdir(os.path.dirname(os.path.abspath(sys.argv[0]))):						#Read al the  files in the current path
	if x.endswith('.vcf'):											#Read only the vcf files
		y=str(x)
		y=y[:-3]+'csv'											#Convert type from .vcf to .csv	
		with open(y,'w') as csv:
			csv.write(',REF,ALT,ALT,')								#Write headstatment in the csv file
			csv.write(y[:-3])
			csv.write('\n')													
			with open(x,'r') as file:
				for line in file:
					if line[0] != '#':
						sp=line.split()							#Skip lines with # at the begin					
						form = sp[9]							#Convert the FORM type from VCF to CSV -> 0|0 -> "0,0"
						try1=sp[0]+';'+sp[1]+','+sp[3]+','				#Split the lines in a list to take only the CHROM,POS,REF,ALT,FORM
						if ',' in sp[4]:						#Consider two posibles ALT 
							try1+= sp[4]+','+'"'+form[0]+','+form[2]+'"'
						elif '.' in sp[4]:						#Case where there's not ALT			
							try1+='.,.,'+'"'+form[0]+','+form[2]+'"'
						else:								#Case with only one ALT
							try1+=sp[4]+','+sp[4]+','+'"'+form[0]+','+form[2]+'"'
						csv.write(try1)							#Write the CSV file
						csv.write('\n')


