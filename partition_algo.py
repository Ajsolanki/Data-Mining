import numpy as np  
import matplotlib.pyplot as plt  
import pandas as pd  
from apyori import apriori  

store_data = pd.read_csv('assosiation_rule.csv')  

#Preprocess the dataset and convert into a list
def ds_preprocessing(dataset):
    records = []  
    for i in range(len(dataset)):  
        records.append([str(dataset.values[i,j]) for j in range(len(list(dataset)))])
    return records

#Gives the frequent itemset
def apriory(dataset):
    set_list = []
    association_rules = apriori(dataset, min_support=0.2, min_confidence=0.2, min_lift=3, min_length=2)  
    association_results = list(association_rules)
    for i in range(len(association_results)):
        set_list.append(association_results[i][0])
    return set_list

#Gives the Global list of frequent itemset
def global_frequent_set(store_data):
    n = int(input("Enter the number of partition of dataset: "))
    ds = np.array_split(store_data, n)

    global_set_list = []

    for i in range(n):
        
        tmp_ds = ds_preprocessing(ds[i])
        x = apriory(tmp_ds)
        global_set_list.append(x)
    return global_set_list
          
     