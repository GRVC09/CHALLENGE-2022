'''
Same structure as ANN.py

'''


import tensorflow as tf
import pickle
import numpy as np
import math
from make_in_ANN import create_feature_sets_and_labels
from make_in_ANN import create_feature_sets
import sys

predict_set=create_feature_sets('UNK_avr.dat')

sess=tf.Session()    
#First let's load meta graph and restore weights
saver = tf.train.import_meta_graph('model1-1000.meta')
saver.restore(sess,tf.train.latest_checkpoint('./'))

n_nodes_hl1 = 100
n_nodes_hl2 = 100
n_nodes_hl3 = 100

n_classes = 5

graph = tf.get_default_graph()

x = tf.placeholder('float')
batch_x = np.array(predict_set[:])
batch_x=np.float32(batch_x)
feed_dict={x:batch_x}

#Load the weights and biases to hidden layers

hidden_1_layer = {'f_fum':n_nodes_hl1,
                  'weight':tf.Variable(sess.run('w1:0')),
                  'bias':tf.Variable(sess.run('b1:0'))}

hidden_2_layer = {'f_fum':n_nodes_hl2,
				  'weight':tf.Variable(sess.run('w2:0')),
                  'bias':tf.Variable(sess.run('b2:0'))}

hidden_3_layer = {'f_fum':n_nodes_hl3,
                  'weight':tf.Variable(sess.run('w3:0')),
                  'bias':tf.Variable(sess.run('b3:0'))}

output_layer = {'f_fum':None,
                'weight':tf.Variable(sess.run('w4:0')),
                  'bias':tf.Variable(sess.run('b4:0'))}

#Compute the output of the network with the load values and the new inputs (predict_set)

sess.run(tf.initialize_all_variables())

l1 = tf.add(tf.matmul(x,hidden_1_layer['weight']), hidden_1_layer['bias'])
l1 = tf.nn.relu(l1)

l2 = tf.add(tf.matmul(l1,hidden_2_layer['weight']), hidden_2_layer['bias'])
l2 = tf.nn.relu(l2)

l3 = tf.add(tf.matmul(l2,hidden_3_layer['weight']), hidden_3_layer['bias'])
l3 = tf.nn.relu(l3)

output = tf.matmul(l3,output_layer['weight']) + output_layer['bias']

#Store the classification and the outputs from ANN

fh=open('classification_results.dat','w')
classification_result=sess.run(output,feed_dict)
for i in range(len(classification_result)):
	for j in range(5):
		fh.write(str(classification_result[i][j]))
		fh.write('\t')
	fh.write('\n')
classification=sess.run(tf.argmax(classification_result,1),feed_dict)
fh=open('classification.dat','w')		
for i in range(len(classification)):
	fh.write(str(classification[i]))
	fh.write('\t')
