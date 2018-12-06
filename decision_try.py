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
    entropy = np.sum([(-att_counts[i]/np.sum(att_counts))*math.log(att_counts[i]/np.sum(att_counts),2) for i in range(len(att_value))])
    return(entropy)

#Counts the unique labels in column 
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

def decision_tree(data):
    d_tree = {}
    
    features = data.iloc[:,:-1].columns
    
    gains = {}
    
    for feature in features:
        gains[feature] = gain(feature)
    
    divide_by = max(gains, key=gains.get)
    
    elements = data.loc[:,divide_by]
    
    d_tree[divide_by] = {}
    for element in np.unique(elements):
        print("Dividing By Column:", divide_by, " at Value:", element)
        
        if len(np.unique(data.loc[data[divide_by]==element,:].iloc[:,-1]))>1:
            
            d_tree[divide_by][element] = decision_tree(data.loc[data[divide_by]==element,:].drop(divide_by,axis=1))
            
        else:
            print("Reached Leaf at Column:", divide_by, " at Value:", element)
            d_tree[divide_by][element] =  str(np.unique(data.loc[data[divide_by]==element,:].iloc[:,-1])[0])
    return d_tree

dataset = pd.read_csv('data.csv')
dataset = dataset.drop("day",axis=1)

dataset.tail()

features = dataset.columns
dtree = decision_tree(dataset)


    

