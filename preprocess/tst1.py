import csv
import numpy as np
from sklearn.model_selection import train_test_split

_X_train = None
_X_test = None
_X_val = None
_Y_train = None
_Y_test = None
_Y_val = None

def get_X_train():
    global _X_train
    return _X_train

def set_X_train(arr):
    global _X_train
    _X_train = arr

def get_X_test():
    global _X_test
    return _X_test

def set_X_test(arr):
    global _X_test
    _X_test = arr

def get_X_val():
    global _X_val
    return _X_val

def set_X_val(arr):
    global _X_val
    _X_val = arr

# ---

def get_Y_train():
    global _Y_train
    return _Y_train

def set_Y_train(arr):
    global _Y_train
    _Y_train = arr

def get_Y_test():
    global _Y_test
    return _Y_test

def set_Y_test(arr):
    global _Y_test
    _Y_test = arr

def get_Y_val():
    global _Y_val
    return _Y_val

def set_Y_val(arr):
    global _Y_val
    _Y_val = arr

def preprocess():

    global _X_train
    global _X_test
    global _X_val
    global _Y_train
    global _Y_test
    global _Y_val

    f = open('participants_79.csv')
    L = [[0 for cols in range(5)] for rows in range(138)]

    win = []
    lose = []

    reader = csv.reader(f)
    a = list(reader)

    #print(a[0])
    #print(a[0][1])

    cnt = 0

    while 1: #조건 수정 

        for i in range(5):              #이긴 팀 
            champs_id = a[cnt][3]   
            L[i][champs_id]=1
            cnt+=1
        result = np.array(L)
        win.append(result)

        for j in range(5):              #진 팀 
            champs_id = a[cnt][3]
            L[j][champs_id]=1
            cnt+=1
        result = np.array(L)
        win.append(result)


    wins = np.array(win)
    loses = np.array(lose)

    _X_train, _X_test, _Y_train, _Y_test = train_test_split(wins, loses, test_size = 0.2, random_state = 1)
    _X_train, _X_val, _Y_train, _Y_val = train_test_split(_X_train, _Y_train, test_size = 0.2, random_state = 1)


            
    



                
    
    
    
      
    
    
