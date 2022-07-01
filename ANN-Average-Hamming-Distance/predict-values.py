dictionary={0:'EUR',1:'AMR',2:'SAS',3:'EAS',4:'AFR'}		#Dictionary for the values in the classification an the continent that represents.
label=[]
reference=[]
with open('Information.txt','r') as info:
	i=0
	while True:
		line=info.readline()
		if not line:
			break
		if i%2 == 0 and i >2:				#Read the reference continent
			ref=line
			ref=ref.split()
		if i%2 == 1 and i >3:				#Read the name of the sample
			split=line.split()
			for j in range(len(split)):			
				label.append(split[j])
				reference.append(ref[0])
		i+=1
predict=open('Prediction.txt','w')
predict.write('Reference					Expected	Prediction')
predict.write('\n')
with open('clasification.dat','r') as dat:			#Read the results of the classification.
	line=dat.readline()
	line=line.split()
	for i in range(len(line)):
		predict.write(label[i])
		predict.write('\t')
		predict.write(reference[i])
		predict.write('\t')
		predict.write(dictionary[int(line[i])])
		predict.write('\n')
