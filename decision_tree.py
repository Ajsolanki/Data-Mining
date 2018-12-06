from __future__ import division
import pandas as pd 
import numpy as np
import math


df = pd.read_csv("data.csv")
column = list(df)

def entropy(att):
   
    value,counts = np.unique(att, return_counts = True)
    entropy = np.sum([-(counts[i]/np.sum(counts))*math.log(counts[i]/np.sum(counts) ,2) for i in range(len(counts))])
    
    return entropy

def count(value,deci_att):
    A = [] 
    B = []
    col1 = deci_att
    col2 = df[column[len(column)-1]]
    
    length_col=len(deci_att)
    
    for i in range(length_col):
        if(col1[i] == value):
            A.append(col1[i])
            B.append(col2[i])
        
    return (entropy(B))
 
def gain(deci_att,target_att="play"):
      target_att_col = df[deci_att]  

      target_value, target_count = np.unique(target_att_col, return_counts = True)
      C = [] 
      decision_entropy = entropy(df["play"])
      
      for i in range(len(target_value)):
          C.append(count(target_value[i],target_att_col))
          
      att_entropy = np.sum([(C[i]*(target_count[i]/np.sum(target_count))) for i in range(len(C)-1)])
             
      Gain = decision_entropy - att_entropy
      return Gain 

