'''
We used this algorithm to model a fully connected artificial neural network. We use 3 hidden layers with 100 neurons per hidden layer. 
We use the TensorFlow 0.11 libraries for developing this model, as well as python2.7. To train the network, we use a method known as 
Cross-Validation, which divides the referenced data set into five subsets (preferably of equal or similar size). The train_x and train_y 
labels are the values of the entire training set (x), as well as their respective expected or target values(y).

'''

import tensorflow as tf
import pickle
import numpy as np
import math
from make_in_ANN import create_feature_sets_and_labels
from make_in_ANN import create_feature_sets
import sys

train_x,train_y,groups = create_feature_sets_and_labels('EUR_ham.dat','AMR_ham.dat','SAS_ham.dat',
		'EAS_ham.dat','AFR_ham.dat')

n_nodes_hl1 = 100
n_nodes_hl2 = 100											#Number of neurons per hidden layer
n_nodes_hl3 = 100

n_classes = 5
hm_epochs = 1000											#Number of epochs to train the ANN

loss = []
accuracy = []

x = tf.placeholder('float',name='x_')									#Start the placeholder for use tensorflow
y = tf.placeholder('float',name='y_')

hidden_1_layer = {'f_fum':n_nodes_hl1,
                  'weight':tf.Variable(tf.random_normal([len(train_x[0]), n_nodes_hl1]),name='w1'),	#This is the structure of the hidden layers, they have n_nodes_hl* neurons
                  'bias':tf.Variable(tf.random_normal([n_nodes_hl1]),name='b1')}			#conected with the input (len(train_x[0]), or with previus hidden layers (n_nodes_hl1,n_nodes_hl2)
													#And in addition, we add the biases to guarantee the non-linearity of the model. The 'name=_' is to 
hidden_2_layer = {'f_fum':n_nodes_hl2,									#store de variables in the saver function of tensorflow
                  'weight':tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2]),name='w2'),
                  'bias':tf.Variable(tf.random_normal([n_nodes_hl2]),name='b2')}

hidden_3_layer = {'f_fum':n_nodes_hl3,
                  'weight':tf.Variable(tf.random_normal([n_nodes_hl2, n_nodes_hl3]),name='w3'),
                  'bias':tf.Variable(tf.random_normal([n_nodes_hl3]),name='b3')}

output_layer = {'f_fum':None,
                'weight':tf.Variable(tf.random_normal([n_nodes_hl3, n_classes]),name='w4'),
                'bias':tf.Variable(tf.random_normal([n_classes]),name='b4')}


def neural_network_model1(x):

    l1 = tf.add(tf.matmul(x,hidden_1_layer['weight']), hidden_1_layer['bias'])				#Here we define the operations described in transforming the network's 
    l1 = tf.nn.relu(l1)											#input into the output. First, we multiply the input of each layer by 
													#its corresponding weight, add the bias and evaluate it in the activation function (relu).
    l2 = tf.add(tf.matmul(l1,hidden_2_layer['weight']), hidden_2_layer['bias'])
    l2 = tf.nn.relu(l2)

    l3 = tf.add(tf.matmul(l2,hidden_3_layer['weight']), hidden_3_layer['bias'])
    l3 = tf.nn.relu(l3)

    output = tf.add(tf.matmul(l3,output_layer['weight']),output_layer['bias'],name='out_network')

    return output


def train_neural_network(x):
	prediction = neural_network_model1(x)
	cost = tf.reduce_mean( tf.nn.softmax_cross_entropy_with_logits(prediction,y) )			#For network training, we use Adam's optimizer with a learning rate of 0.001, and to minimize 
	optimizer = tf.train.AdamOptimizer(learning_rate=0.001).minimize(cost)				#the cost function we use the cross_entropy_with_logits method. We use the .train.saver to 
	saver = tf.train.Saver()									#save the variables in a file named 'model1'.meta
	with tf.Session() as sess:
		sess.run(tf.initialize_all_variables())
	    
		for epoch in range(hm_epochs):
			print('Training epoch ',epoch,'/',hm_epochs)
			
			accuracy_aux=0
			loss_aux=0
			for i in range(5):								#Implementation of the Cross-Validation method.
				epoch_loss = 0
				for j in range(5):				
					if i != j:
						start=groups[j][0]
						end=groups[j][1]-1
						batch_x = np.array(train_x[start:end])
						batch_y = np.array(train_y[start:end])
						_, c = sess.run([optimizer, cost], feed_dict={x: batch_x,	#We trained with four subgroups and
				        		                                        y: batch_y})
						epoch_loss += c/(groups[j][1]-groups[j][0])
				correct = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1))
				accuracy1 = tf.reduce_mean(tf.cast(correct, 'float'))
				accu1=accuracy1.eval({x:train_x[groups[i][0]:groups[i][1]-1], y:train_y[groups[i][0]:groups[i][1]-1]})	#Test (evaluated) the rest
				accuracy_aux+=accu1/5.0
				loss_aux+=epoch_loss/5.0
			loss.append(loss_aux)
			accuracy.append(accuracy_aux)

		save_path = saver.save(sess, 'model1',global_step=epoch+1)						#At the end of the training step, we stored the variables in the model1-1000
		
		print("Model saved in path: %s" % save_path)

train_neural_network(x)

f= open("perdida_3Capas_100_100_100.txt","w+")										#Write the loss and accuracy for each cycle
g= open("acierto_3Capas_100_100_100.txt","w+")

for i in range(len(accuracy)):
	a=str(accuracy[i])
	l=str(loss[i])
	f.write(l)
	f.write('\n')
	g.write(a)
	g.write('\n')
f.close()
g.close()
