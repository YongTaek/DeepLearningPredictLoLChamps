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
from preprocess.tst1 import *

preprocess() # in tst1.

learning_rate = 0.001
n_epochs = 20
batch_size = 100
display_step = 1

# 5 input, 1 output
def makeFirstData(x, y):
  return x, y[0]

# 6 input, 1 output
def makeSecondData(x, y):
  x = np.concatenate((x,[y[0]]),axis=0)
  return x, y[1]

# 7 input, 1 output
def makeThirdData(x, y):
  x = np.concatenate((x,y[0:2]),axis=0)
  return x, y[2]

# 8 input, 1 output
def makeFourthData(x, y):
  x = np.concatenate((x,y[0:3]),axis=0)
  return x, y[3]

# 9 input, 1 output
def makeFifthData(x, y):
  x = np.concatenate((x,y[:4]), axis=0)
  return x, y[4]

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
  
  X_batch, X_remain_test, Y_batch, Y_remain_test = train_test_split(get_X_test(), get_Y_test(), shuffle=True, train_size=batch_size)
  
  set_X_test(X_remain_test) # in tst1.py
  set_Y_test(Y_remain_test) # in tst1.py
  
  return X_batch, Y_batch

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

  Y_batches = np.transpose(Y_batches, (1,0,2))

  new_Y_batches = []
  for i in Y_batches:
    new_Y_batches.append(yidsToTrainYids(i))

  new_Y_batches = np.transpose(new_Y_batches, (1,0,2))

  return X_batches, new_Y_batches


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

def yidsToTrainYids(ys): #(5,100,138)
  TrainYids = []

  index0 = np.argmax(ys[0])
  index1 = np.argmax(ys[1])
  index2 = np.argmax(ys[2])
  index3 = np.argmax(ys[3])
  index4 = np.argmax(ys[4])

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
    ys[2] = minus2ids(ys[2], index2)
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


  return TrainYids



def plus1ids(y, index):
  y[index] = 0
  y[index+1] = 1
  return y

def plus2ids(y, index):
  y[index] = 0
  y[index +2] = 1
  return y

def plus3ids(y, index):
  y[index] = 0
  y[index +3] = 1
  return y

def plus4ids(y, index):
  y[index] = 0
  y[index +4] = 1
  return y

def trainYidsToYids(trainYs): # trainYids -> _Yids 
  _Yids = [] 
  
  index0 = trainYs[0].index(1)
  index1 = trainYs[1].index(1)
  index2 = trainYs[2].index(1)
  index3 = trainYs[3].index(1)
  index4 = trainYs[4].index(1)
  
  _Yids.append(trainYs[0]) 

  
  if index0 < index1:  
    _Yids.append(trainYs[1])
  else:
    trainYs[1] = plus1ids(trainYs[1], index1)
    _Yids.append(trainYs[1])
      
  count2 = 0
  if index0 < index2:
    count2 += 1
  if index1 < index2:
    count2 += 1
  if count2 == 0:
    _Yids.append(trainYs[2])
  elif count2 == 1:
    trainYs[2] = plus1ids(trainYs[2], index2)
    _Yids.append(trainYs[2])
  elif count2 == 2:
    trainYs[2] = plus2ids(trainYs[2], index3)
    _Yids.append(trainYs[2])

  count3 = 0
  if index0 < index3:
    count3 += 1
  if index1 < index3:
    count3 += 1
  if index2 < index3:
    count3 += 1
  if count3 == 0:
    _Yids.append(trainYs[3])
  elif count3 == 1:
    trainYs[3] = plus1ids(trainYs[3], index3)
    _Yids.append(trainYs[3])
  elif count3 == 2:
    trainYs[3] = plus2ids(trainYs[3], index3)
    _Yids.append(trainYs[3])
  elif count3 == 3:
    trainYs[3] = plus3ids(trainYs[3], index3)
    _Yids.append(trainYs[3])
      
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
    _Yids.append(trainYs[4])
  elif count4 == 1:
    trainYs[4] = plus1ids(trainYs[4], index4)
    _Yids.append(trainYs[4])
  elif count4 == 2:
    trainYs[4] = plus2ids(trainYs[4], index4)
    _Yids.append(trainYs[4])
  elif count4 == 3:
    trainYs[4] = plus3ids(trainYs[4], index4)
    _Yids.append(trainYs[4])
  elif count4 == 4:
    trainYs[4] = plus4ids(trainYs[4], index4)
    _Yids.append(trainYs[4])

# Network Parameters
n_hidden_1 = 256 # 1st layer number of features
n_hidden_2 = 256 # 2nd layer number of features
n_input = [5*138,6*138,7*138,8*138,9*138] # lose data + win data input (img shape: 28*28)
n_classes = [138,137,136,135,134] # 1 win champs total classes (0-9 digits)

Xs = []
Ys = []
for k, (i, c) in enumerate(zip(n_input, n_classes)):
  X = tf.placeholder(tf.float32, [batch_size, i])
  Y = tf.placeholder(tf.float32, [batch_size, c])
  Xs.append(X)
  Ys.append(Y)

# Create model
def multilayer_perceptron(x, weights, biases,n_input):
    # Hidden layer
    layer_1 = tf.add(tf.matmul(x, weights['n'+str(n_input)]), biases['b1'])
    layer_1 = tf.nn.relu(layer_1)
    # Hidden layer
    layer_2 = tf.add(tf.matmul(layer_1, weights['h2']), biases['b2'])
    layer_2 = tf.nn.relu(layer_2)
    # Output layer with linear activation
    out_layer = tf.matmul(layer_2, weights['out'+str(n_input)]) + biases['out'+str(n_input)]
    return out_layer

# Store layers weight & bias
weights = {
    'n1': tf.Variable(tf.random_normal([n_input[0], n_hidden_1])),
    'n2': tf.Variable(tf.random_normal([n_input[1], n_hidden_1])),
    'n3': tf.Variable(tf.random_normal([n_input[2], n_hidden_1])),
    'n4': tf.Variable(tf.random_normal([n_input[3], n_hidden_1])),
    'n5': tf.Variable(tf.random_normal([n_input[4], n_hidden_1])),
    'h2': tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2])),
    'out1': tf.Variable(tf.random_normal([n_hidden_2, n_classes[0]])),
    'out2': tf.Variable(tf.random_normal([n_hidden_2, n_classes[1]])),
    'out3': tf.Variable(tf.random_normal([n_hidden_2, n_classes[2]])),
    'out4': tf.Variable(tf.random_normal([n_hidden_2, n_classes[3]])),
    'out5': tf.Variable(tf.random_normal([n_hidden_2, n_classes[4]]))
}

biases = {
    'b1': tf.Variable(tf.random_normal([n_hidden_1])),
    'b2': tf.Variable(tf.random_normal([n_hidden_2])),
    'out1': tf.Variable(tf.random_normal([n_classes[0]])),
    'out2': tf.Variable(tf.random_normal([n_classes[1]])),
    'out3': tf.Variable(tf.random_normal([n_classes[2]])),
    'out4': tf.Variable(tf.random_normal([n_classes[3]])),
    'out5': tf.Variable(tf.random_normal([n_classes[4]]))
}

# Construct model
models = []
for k in range(5):
  pred = multilayer_perceptron(Xs[k], weights, biases,k+1)
  models.append(pred)

losses = []
# Define loss and optimizer
for pred,Y in zip(models, Ys):
  loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=pred, labels=Y))
  losses.append(loss)

optimizers = []
for loss in losses:
  optimizer = tf.train.RMSPropOptimizer(learning_rate=learning_rate).minimize(loss)
  optimizers.append(optimizer)

# Launch the graph
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    
    # make 5 models, losses, optimizers
    n_batches = int(len(get_X_train()) / batch_size)  # TODO : confirm

    # Training 
    for i in range(n_epochs):
        total_loss = [0.,0.,0.,0.,0.]
        init_train()
        # Loop over all batches
        for j in range(n_batches):
          
            X_batch, Y_batch = get_rand_trainset(batch_size)
            X_batches, Y_batches = makeBatchData(X_batch, Y_batch)
            
            # Run optimization op (backprop) and cost op (to get loss value)
            # run 5 optimizers
            for k,(x_batch, y_batch) in enumerate(zip(X_batches, Y_batches)):
              x_batch = np.reshape(x_batch, [batch_size, len(x_batch[0])*len(x_batch[0][0])])
              if k != 0:
                new_y_batch = []
                for l in range(100):
                  new_y_batch.append(y_batch[l][:-k])
              else:
                new_y_batch = y_batch
              _, l = sess.run(
                  [optimizers[k], losses[k]], feed_dict={Xs[k]: x_batch, Ys[k]: new_y_batch})   
              # Compute average loss
              total_loss[k] += l
            # _, l = sess.run([optimizer, loss], feed_dict={X: X_batch, Y: Y_batch})
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
        accuracy_batch = []
        for k,(x_batch,y_batch) in enumerate(zip(X_batches,Y_batches)):
            if k != 0:
                new_y_batch = []
                for l in range(100):
                    new_y_batch.append(y_batch[l][:-k])
            else:
                new_y_batch = y_batch

            
            # 5,138
            x_batch = np.reshape(x_batch, [batch_size, len(x_batch[0]) * len(x_batch[0][0])])
            accuracy_batch.append(sess.run(accuracy_set[k], feed_dict={Xs[k]: x_batch, Ys[k]: new_y_batch}))
            total_correct_preds[k] += accuracy_batch[k]
    
    order=['First','Second','Third','Fourth','Fifth']
    all_total_correct_preds = 0
    for correct_preds,o in zip(total_correct_preds,order):
        all_total_correct_preds += correct_preds
        print(o,'data_accuracy {0}'.format(correct_preds/len(get_X_test())))
        
    
    print('Accuracy {0}'.format(all_total_correct_preds/5))

