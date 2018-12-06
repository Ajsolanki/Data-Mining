#!/usr/bin/python3 -i
import pandas as pd
import numpy as np
import math
from pprint import pprint

data = pd.read_csv('data.csv',names=['day','outlook','temp',
                                'humidity','wind','play','class'])

def entropy(target_col):
    
    elements,counts = np.unique(target_col,return_counts = True)
    
    for i in range(len(elements)):
       
        #entropy = (-counts[i])/len(target_col)*math.log(counts[i]/len(target_col),len(counts))
        entropy = np.sum([(-counts[i]/np.sum(counts))*math.log(counts[i]/np.sum(counts),len(counts))])
        return entropy


def InfoGain(data,split_attribute_name,target_name="class"):
        
    #Calculate the entropy of the total dataset
    total_entropy = entropy(data[target_name])
    
    ##Calculate the entropy of the dataset
    
    #Calculate the values and the corresponding counts for the split attribute 
    vals,counts= np.unique(data[split_attribute_name],return_counts=True)
    
    #Calculate the weighted entropy
    Weighted_Entropy = np.sum([(counts[i]/np.sum(counts))*entropy(data.where(data[split_attribute_name]==vals[i]).dropna()[target_name]) for i in range(len(vals))])
    
    #Calculate the information gain
    Information_Gain = total_entropy - Weighted_Entropy
    return Information_Gain