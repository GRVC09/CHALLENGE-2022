import numpy as np
import random
import math

def sample_handling(sample,clasification):

	features=[]
	features=list(features)
	for i in sample:
		features.append([i,clasification])

	return(features)


def create_feature_sets_and_labels(EUR,AMR,SAS,EAR,AFR):
	
	features = []
	EU=np.loadtxt(EUR)
	AM=np.loadtxt(AMR)
	SA=np.loadtxt(SAS)
	EA=np.loadtxt(EAR)
	AF=np.loadtxt(AFR)

	s_EU=[1,0,0,0,0]
	s_AM=[0,1,0,0,0]
	s_SA=[0,0,1,0,0]
	s_EA=[0,0,0,1,0]
	s_AF=[0,0,0,0,1]

	s_EU=np.array(s_EU)
	s_AM=np.array(s_AM)
	s_SA=np.array(s_SA)
	s_EA=np.array(s_EA)
	s_AF=np.array(s_AF)

	features += sample_handling(EU,s_EU)
	features += sample_handling(AM,s_AM)
	features += sample_handling(SA,s_SA)	
	features += sample_handling(EA,s_EA)
	features += sample_handling(AF,s_AF)	


	random.shuffle(features)
	features = np.array(features)
	train_x = list(features[:][:,0])
	train_y = list(features[:][:,1])


	size_test=0.2
	test_len=int(size_test*len(train_x))
	train_len=int(math.ceil((1-size_test)*len(train_x))/4)
	groups=[]
	n=0
	for i in range(5):
		if i < 4:
			groups.append([n,n+train_len])
			n+=train_len
		else:
			groups.append([n,n+test_len])
			n+=test_len

	return train_x,train_y,groups

def create_feature_sets(UNK):
	features = []
	UN=np.loadtxt(UNK)

	s_UN=[0,0,0,0,0]

	s_UN=np.array(s_UN)

	features += sample_handling(UN,s_UN)	

	features = np.array(features)
	features_x = list(features[:][:,0])

	return features_x

if __name__ == '__main__':
	train_x,train_y,groups = create_feature_sets_and_labels('EUR_avr.dat','AMR_avr.dat','SAS_avr.dat',
		'EAS_avr.dat','AFR_avr.dat')
	features_x = create_feature_sets('UNK_avr.dat')
