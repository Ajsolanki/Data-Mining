# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 11:16:28 2018

@author: Aj
"""

import pandas as pd 
import math
import numpy as np
import random

K = 3

data = pd.read_csv("data_auc.csv")

column = list(data)


def preprocess_data(dataset):
    data_list = []
    
    for i in range(len(data)):
        data_list.append([dataset.values[i,j] for j in range(1,len(column))])
    return data_list

process_data = preprocess_data(data)
test_data = random.sample(process_data,round(0.25*len(process_data)))
training_data = []
for i in process_data:
    if i in test_data:
        continue
    else:
        training_data.append(i)


#Calculate the distance between two given points
def distance(query_list,set_of_pt):
    dis = math.sqrt(((query_list[0]-set_of_pt[0])*(query_list[0]-set_of_pt[0]))+ ((query_list[1]-set_of_pt[1])*(query_list[1]-set_of_pt[1])))
    return round(dis,2)

#Gives the K nearest neighbor
def score(query,k=K):
    temp_list = []
    
    for i in range(len(training_data)):
        temp = distance(query,training_data[i])
        temp_list.append((temp,training_data[i][2]))
    temp_list = sorted(temp_list)
    
    count = 0
    for i in range(K):
        if temp_list[i][1] == 1:
            count += 1
    return float(count/K)
        

def auc(test_dataset):
    pos,neg = [],[]
    for i in test_data:
        if i[2]==1:
            pos.append(i) 
        if i[2]==-1:
            neg.append(i)
    count_list = []
    count = 0
    for i in pos:
        for j in neg:
            temp_pos = score(i)
            temp_neg = score(j)
            if temp_pos > temp_neg:
                count = 1
            elif temp_pos == temp_neg:
                count = 0.5
            else:
                count = 0
            count_list.append(count)
    auc = np.sum(count_list)/(len(neg)*len(pos))
    print("Negative Test instances is :" ,neg)
    print("Postive Test Instances is :" ,pos)
    print("Count of S(Xi,Xj) is: " ,count_list)
    return print("AUC is:",auc)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    