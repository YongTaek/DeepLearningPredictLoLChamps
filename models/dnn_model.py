# -*- coding: utf-8 -*-
"""dnn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xDMHppfAy2hIFWBMIs_PbcXWla7hFH10
"""

import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'


import tensorflow as tf
from sklearn.model_selection import train_test_split
from tst1 import *

preprocess() # in tst1.py

learning_rate = 0.001
n_epochs = 20
batch_size = 100
display_step = 1

# 5 input, 1 output
def makeFirstData(x, y):
  return x, y[0]

# 6 input, 1 output
def makeSecondData(x, y):
  return x + y[0], y[1]

# 7 input, 1 output
def makeThirdData(x, y):
  return x + y[0:2], y[2]

# 8 input, 1 output
def makeFourthData(x, y):
  return x + y[0:3], y[3]

# 9 input, 1 output
def makeFifthData(x, y):
  return x + y[:4], y[4]

def get_rand_trainset(batch_size):
  
  # win : [[[0,0,...1,0,...0],[0,0,...1,0,...0],[0,0,...1,0,...0],[0,0,...1,0,...0],[0,0,...1,0,...0]], <- match1
  #        [[0,0,...1,0,...0],[0,0,...1,0,...0],[0,0,...1,0,...0],[0,0,...1,0,...0],[0,0,...1,0,...0]], <- match2]
  
  # return : batch크기의 win, batch크기의 lose
  
  X_batch, X_remain_train, y_batch, y_remain_train = train_test_split(get_X_train(), get_Y_train(), shuffle=True, train_size=batch_size)
  
  set_X_train(X_remain_train) # in tst1.py
  set_Y_train(y_remain_train) # in tst1.py
  
  return X_batch, y_batch

def get_rand_testset(batch_size):
  
  # win : [[[0,0,...1,0,...0],[0,0,...1,0,...0],[0,0,...1,0,...0],[0,0,...1,0,...0],[0,0,...1,0,...0]], <- match1
  #        [[0,0,...1,0,...0],[0,0,...1,0,...0],[0,0,...1,0,...0],[0,0,...1,0,...0],[0,0,...1,0,...0]], <- match2]
  
  # return : batch크기의 win, batch크기의 lose,
  
  X_batch, X_remain_test, y_batch, y_remain_test = train_test_split(get_X_test(), get_Y_test(), shuffle=True, train_size=batch_size)
  
  set_X_test(X_remain_test) # in tst1.py
  set_Y_test(Y_remain_test) # in tst1.py
  
  return X_batch, y_batch

def makeBatchData(X_batch, Y_batch):
  X_batches = []
  Y_batches = []
  
  first_X_batch = [makeFirstData(x,y)[0] for x, y in zip(X_batch, Y_batch)]
  first_Y_batch = [makeFirstData(x,y)[1] for x, y in zip(X_batch, Y_batch)]
  X_batches.append(first_X_batch)
  Y_batches.append(first_Y_batch)    
  
  second_X_batch = [makeSecondData(x,y)[0] for x, y in zip(X_batch, Y_batch)]
  second_Y_batch = [makeSecondData(x,y)[1] for x, y in zip(X_batch, Y_batch)]
  X_batches.append(second_X_batch)
  Y_batches.append(second_Y_batch) 
  
  third_X_batch = [makeThirdData(x,y)[0] for x, y in zip(X_batch, Y_batch)]
  third_Y_batch = [makeFourthData(x,y)[1] for x, y in zip(X_batch, Y_batch)]
  X_batches.append(third_X_batch)
  Y_batches.append(third_Y_batch)    

  
  fourth_X_batch = [makeFourthData(x,y)[0] for x, y in zip(X_batch, Y_batch)]
  fourth_Y_batch = [makeFourthData(x,y)[1] for x, y in zip(X_batch, Y_batch)]
  X_batches.append(fourth_X_batch)
  Y_batches.append(fourth_Y_batch)    
  
  
  fifth_X_batch = [makeFifthData(x,y)[0] for x, y in zip(X_batch, Y_batch)]
  fifth_Y_batch = [makeFifthData(x,y)[1] for x, y in zip(X_batch, Y_batch)]
  X_batches.append(fifth_X_batch)
  Y_batches.append(fifth_Y_batch) 
  
  
  return X_batches, Y_batches

def yidsToTrainYids_old(ys):
  TrainYids = []
  
  index0 = ys[0].index(1)
  index1 = ys[1].index(1)
  index2 = ys[2].index(1)
  index3 = ys[3].index(1)
  index4 = ys[4].index(1)
  
  TrainYids.append(ys[0])

  
  if index0 > index1:
    TrainYids.append(ys[1])
  else:
    ys[1] = minus1ids(ys[1], index1)
    TrainYids.append(ys[1])
    
  if index0 < index1:
    if index0 > index2:
      TrainYids.append(ys[2])
    elif index0 < index2 and index2 < index1:
      ys[2] = minus1ids(ys[2], index2)
      TrainYids.append(ys[2])
    else:
      ys[2] = minus2ids(ys[2], index2)
      TrainYids.append(ys[2])
  else:
    if index1 > index2:
      TrainYids.append(ys[2])
    elif index1 < index2 and index2 < index0:
      ys[2] = minus1ids(ys[2], index2)
      TrainYids.append(ys[2])
    else:
      ys[2] = minus2ids(ys[2], index2)
      TrainYids.append(ys[2])
      
      
  if index0 < index1 and index1 < index2:
    if index3 > index2:
      ys[3] = minus3ids(ys[3], index3)
      TrainYids.append(ys[3])
    elif index1 < index3:
      ys[3] = minus2ids(ys[3], index3)
      TrainYids.append(ys[3])
    elif index0 < index3:
      ys[3] = minus1ids(ys[3], index3)
      TrainYids.append(ys[3])
    else:
      TrainYids.append(ys[3])
  elif index0 < index2 and index2 < index1:
    if index3 > index1:
      ys[3] = minus3ids(ys[3], index3)
      TrainYids.append(ys[3])
    elif index2 < index3:
      ys[3] = minus2ids(ys[3], index3)
      TrainYids.append(ys[3])
    elif index0 < index3:
      ys[3] = minus1ids(ys[3], index3)
      TrainYids.append(ys[3])
    else:
      TrainYids.append(ys[3])
  elif index1 < index0 and index0 < index2:
    if index2 < index3:
      ys[3] = minus3ids(ys[3], index3)
      TrainYids.append(ys[3])
    elif index0 < index3:
      ys[3] = minus2ids(ys[3], index3)
      TrainYids.append(ys[3])
    elif index1 < index3:
      ys[3] = minus1ids(ys[3], index3)
      TrainYids.append(ys[3])
    else:
      TrainYids.append(ys[3])
  elif index1 < index2 and index2 < index0:
    if index0 < index3:
      ys[3] = minus3ids(ys[3], index3)
      TrainYids.append(ys[3])
    elif index2 < index3:
      ys[3] = minus2ids(ys[3], index3)
      TrainYids.append(ys[3])
    elif index1 < index3:
      ys[3] = minus1ids(ys[3], index3)
      TrainYids.append(ys[3])
    else:
      TrainYids.append(ys[3])
  elif index2 < index0 and index0 < index1:
    if index1 < index3:
      ys[3] = minus3ids(ys[3], index3)
      TrainYids.append(ys[3])
    elif index0 < index3:
      ys[3] = minus2ids(ys[3], index3)
      TrainYids.append(ys[3])
    elif index2 < index3:
      ys[3] = minus1ids(ys[3], index3)
      TrainYids.append(ys[3])
    else:
      TrainYids.append(ys[3])
  elif index2 < index1 and index1 < index0:
    if index0 < index3:
      ys[3] = minus3ids(ys[3], index3)
      TrainYids.append(ys[3])
    elif index1 < index3:
      ys[3] = minus2ids(ys[3], index3)
      TrainYids.append(ys[3])
    elif index2 < index3:
      ys[3] = minus1ids(ys[3], index3)
      TrainYids.append(ys[3])
    else:
      TrainYids.append(ys[3])

def minus1ids(y, index):
  y[index] = 0
  y[index-1] = 1
  return y

def minus2ids(y, index):
  y[index] = 0
  y[index -2] = 1
  return y

def minus3ids(y, index):
  y[index] = 0
  y[index -3] = 1
  return y

def minus4ids(y, index):
  y[index] = 0
  y[index -4] = 1
  return y

def yidsToTrainYids(ys):
  TrainYids = []
  
  index0 = ys[0].index(1)
  index1 = ys[1].index(1)
  index2 = ys[2].index(1)
  index3 = ys[3].index(1)
  index4 = ys[4].index(1)
  
  TrainYids.append(ys[0])

  
  if index0 > index1:
    TrainYids.append(ys[1])
  else:
    ys[1] = minus1ids(ys[1], index1)
    TrainYids.append(ys[1])
      
  count2 = 0
  if index0 < index2:
    count2 += 1
  if index1 < index2:
    count2 += 1
  if count2 == 0:
    TrainYids.append(ys[2])
  elif count2 == 1:
    ys[2] = minus1ids(ys[2], index2)
    TrainYids.append(ys[2])
  elif count2 == 2:
    ys[2] = minus2ids(ys[2], index3)
    TrainYids.append(ys[2])

  count3 = 0
  if index0 < index3:
    count3 += 1
  if index1 < index3:
    count3 += 1
  if index2 < index3:
    count3 += 1
  if count3 == 0:
    TrainYids.append(ys[3])
  elif count3 == 1:
    ys[3] = minus1ids(ys[3], index3)
    TrainYids.append(ys[3])
  elif count3 == 2:
    ys[3] = minus2ids(ys[3], index3)
    TrainYids.append(ys[3])
  elif count3 == 3:
    ys[3] = minus3ids(ys[3], index3)
    TrainYids.append(ys[3])
      
  count4 = 0
  if index0 < index4:
    count4 += 1
  if index1 < index4:
    count4 += 1
  if index2 < index4:
    count4 += 1
  if index3 < index4:
    count4 += 1
  if count4 == 0:
    TrainYids.append(ys[4])
  elif count4 == 1:
    ys[4] = minus1ids(ys[4], index4)
    TrainYids.append(ys[4])
  elif count4 == 2:
    ys[4] = minus2ids(ys[4], index4)
    TrainYids.append(ys[4])
  elif count4 == 3:
    ys[4] = minus3ids(ys[4], index4)
    TrainYids.append(ys[4])
  elif count4 == 4:
    ys[4] = minus4ids(ys[4], index4)
    TrainYids.append(ys[4])

def trainYidsToYids(trainYs):

# Network Parameters
n_hidden_1 = 256 # 1st layer number of features
n_hidden_2 = 256 # 2nd layer number of features
n_input = [5*138,6*138,7*138,8*138,9*138] # lose data + win data input (img shape: 28*28)
n_classes = [138,137,136,135,134] # 1 win champs total classes (0-9 digits)

# tf Graph input
def makePlaceholder(batch_size, n_input, n_classes):
  X = tf.placeholder(tf.float32, [batch_size, n_input])
  Y = tf.placeholder(tf.float32, [batch_size, n_classes])
  return X, Y

# Create model
def multilayer_perceptron(x, weights, biases):
    # Hidden layer
    layer_1 = tf.add(tf.matmul(x, weights['h1']), biases['b1'])
    layer_1 = tf.nn.relu(layer_1)
    # Hidden layer
    layer_2 = tf.add(tf.matmul(layer_1, weights['h2']), biases['b2'])
    layer_2 = tf.nn.relu(layer_2)
    # Output layer with linear activation
    out_layer = tf.matmul(layer_2, weights['out']) + biases['out']
    return out_layer

# Store layers weight & bias
weights = {
    'h1': tf.Variable(tf.random_normal([n_input, n_hidden_1])),
    'h2': tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2])),
    'out': tf.Variable(tf.random_normal([n_hidden_2, n_classes]))
}

biases = {
    'b1': tf.Variable(tf.random_normal([n_hidden_1])),
    'b2': tf.Variable(tf.random_normal([n_hidden_2])),
    'out': tf.Variable(tf.random_normal([n_classes]))
}

# Construct model
def makeModel(weights, biases):
  models = []
  Ys = []
  for i in n_input:
    X, Y = makePlaceholder(batch_size, i, n_classes)
    pred = multilayer_perceptron(X, weights, biases)
    models.append(pred)
    Ys.append(Y)
  return models, Ys

def makeLosses(models, Ys):
  losses = []
  # Define loss and optimizer
  for pred,Y in zip(models, Ys):
    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=pred, labels=Y))
    losses.append(loss)
  return losses

def makeOptimizer(losses):
  optimizers = []
  for loss in losses:
    optimizer = tf.train.RMSPropOptimizer(learning_rate=learning_rate).minimize(loss)
    optimizers.append(optimizer)
  return optimizers

# Launch the graph
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    
    # make 5 models, losses, optimizers
    models, Ys = makeModel(weights, biases)
    losses = makeLosses(models,Ys)
    optimizers = makeOptimizer(losses)
    
    # Training 
    for i in range(n_epochs):
        total_loss = [0.,0.,0.,0.,0.]
        n_batches = int(len(get_X_train())/batch_size) # TODO : confirm
        # Loop over all batches
        for j in range(n_batches):
          
            X_batch, Y_batch = get_rand_trainset(batch_size)
            X_batches, Y_batches = makeBatchData(X_batch, Y_batch)
            
            # Run optimization op (backprop) and cost op (to get loss value)
            # run 5 optimizers
            for k,(x_batch, y_batch) in enumerate(zip(X_batches, Y_batches)):
              _, l = sess.run([optimizers[k], losses[k], feed_dict={X: x_batch, Y: y_batch}])
              # Compute average loss
              total_loss[k] += l
            #_, l = sess.run([optimizer, loss], feed_dict={X: X_batch, Y: Y_batch})
            # Compute average loss
            #total_loss += l
        # Display logs per epoch step
        for loss in total_loss:
          print('Average loss epoch {0}: {1}'.format(i, loss/n_batches))

    print("Optimization Finished!")


    
    #TODO: pred -> models 중 하나로 변경
    
    #correct_preds_set=[]
    accuracy_set=[]
    for pred,Y in zip(models,Ys):
        correct_preds = tf.equal(tf.argmax(pred, axis=1), tf.argmax(Y, axis=1))#true, false개수가 총 배치사이즈 개수만큼
        accuracy = tf.reduce_sum(tf.cast(correct_preds, tf.float32))#true 개수(최대 배치사이즈 개수(정수값))
        #correct_preds_set.append(correct_preds)
        accuracy_set.append(accuracy)
    
    n_batches = int(len(get_X_test())/batch_size)
    total_correct_preds = [0,0,0,0,0]
    
        for i in range(n_batches):
            X_batch, Y_batch = get_rand_testset(batch_size)
            X_batches,Y_batches=makeBatchData(X_batch,Y_batch)
            for k,(x_batch,y_batch) in enumerate(zip(X_batches,Y_batches)):
                accuracy_batch[k] = sess.run(accuracy_set[k], feed_dict={X: X_batch, Y:Y_batch})#정수값 
                total_correct_preds[k] += accuracy_batch
    
    order=['First','Second','Third','Fourth','Fifth']
    for correct_preds,o in zip(total_correct_preds,order):
        all_total_correct_preds += correct_preds
        print(o,'data_accuracy {0}'.format(correct_preds/get_X_test()))
        
    
    print('Accuracy {0}'.format(all_total_correct_preds/5))

