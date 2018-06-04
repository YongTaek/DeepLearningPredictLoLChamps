import csv
import numpy as np



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
            ++cnt
        result = np.array(L)
        win.append(result)

        for j in range(5):              #진 팀 
            champs_id = a[cnt][3]
            L[j][champs_id]=1
            ++cnt
        result = np.array(L)
        win.append(result)


    wins = np.array(win)
    loses = np.array(lose)


    # #readerr = csv.reader(f)
    #next(reader) 
    # #print(list(readerr))
    # for row in reader:
         
        # champs_id = row[2] #If champs_id row num is 2 
        
        # for i in range(5):
        #     L[i][champs_id] = 1
        
    #     result = np.array(L)
    #     win.append(result)
         

    #     for j in range(5):
    #         L[i][champs_id] = 1
        
    #     result = np.array(L)
    #     lose.append(result)


        
    



                
    
    
    
      
    
    