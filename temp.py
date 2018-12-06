#!/usr/bin/python3 -i
from __future__ import division
import pandas as pd
import numpy as np
import math
from pprint import pprint

dataset = pd.read_csv('data.csv')

column = list(dataset)

#Get Entropy with attribute column name 
def entropy(attribute):
    att_value,att_counts = np.unique(attribute, return_counts = True)
    entropy = np.sum([(-att_counts[i]/np.sum(att_counts))*math.log(att_counts[i]/np.sum(att_counts) ,2) for i in range(len(att_value))])
    return(entropy)

#Counts the unique labels in column and give the Entropy 
def count(value,target_att):
    x = []
    y = []
    att1_col = target_att
    att2_col = dataset[column[len(column)-1]]
       
    length_col = len(target_att)
        
    for i in range(length_col):
        if (att1_col[i]==value):
            x.append(att1_col[i])
            y.append(att2_col[i])
        
    return(entropy(y))
        
#Calculate the Gain 
def gain(target_att, decision_att= "decision_column"):
    t=list(dataset)
    decision_att = t[-1]
    target_att_col = dataset[target_att]
    #decision_att_col = dataset[column[len(column)-1]]

    target_value, target_count = np.unique(target_att_col, return_counts = True)
    z=[]
    decision_entropy = entropy(dataset.iloc[:,-1])
    for i in range(len(target_value)):
        z.append(count(target_value[i],target_att_col))
    
    weighted_entropy = np.sum([(z[i]*(target_count[i]/np.sum(target_count))) for i in range(len(z))])
    
    Gain = decision_entropy - weighted_entropy
    return Gain 

#Given dataset name and Get all column gain
def get_all_gain(dataset):
    dataset = pd.read_csv(dataset)
    col = list(dataset)

    print("Entropy of decision label ", entropy(dataset.iloc[:,-1]))
    for att_name in range(1, len(col)-1):
        g = gain(col[att_name])
        print("Gain of "+col[att_name]+ " is : ", g)
    

def root_node(dataset):
    list_col = []
   
    for i in column:
        list_col.append(gain(i))
    return(max(list_col))
    