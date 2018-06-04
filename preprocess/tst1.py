import csv
import numpy as np
from sklearn.model_selection import train_test_split


with open('participants_79.csv') as f:
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

    X_train, X_test, Y_train, Y_test = train_test_split(wins, loses, test_size = 0.2, random_state = 1)
    X_train, X_val, Y_train, Y_val = train_test_split(X_train, Y_train, test_size = 0.2, random_state = 1)


        
    



                
    
    
    
      
    
    
