import numpy as np
import pandas as pd
import itertools as iter

dataset = pd.read_csv("assosiation_rule.csv")

total_trans = dataset[list(dataset)[0]].count()

#Check for the item is in transaction or not
def check(item_set, transaction):
    flag = False
    
    for i in item_set:
        if i in transaction:
            flag = True
        else:
            flag = False
            break
    return flag

#Total count  0f a item in dataset
def count(item_list):
    val = 0
    for j in range(total_trans):
            trans = list(dataset.loc[j])
            if check(item_list, trans)== True:
                val = val + 1
    return val

#Give item-set value and it gives all possible combinations 
def create_set(list_of_item,n):

    set_list = list(iter.combinations(list_of_item, n))
    return set_list

#Calculate the support             
def support(item_list):
    if len(item_list)==1:
        support = count(item_list)/total_trans
    else:
        lis = []
        for i in range(len(item_list)):
            for j in range(len(item_list[0])):
                lis.append(item_list[i][j])
                unique_list = list(set(lis))
        support = count(unique_list)/total_trans

    return support 

#Calculate Confidence of a item 
def confidence(item_set):
    temp=[]
    temp.append(item_set[0])
    return (count(item_set)/count(temp))


#Count total unique items of a dataset 
def count_unique_item(dataset):
    unique_list = []
    for i in list(dataset):
        for  j in dataset[i]:
            unique_list.append(j)
    unique_list = list(set(unique_list))
    u_l = []
    for i in unique_list:
        if(type(i)==str):
            u_l.append(i)
    return u_l

#Give item list and stage no and It gives frequnt item set at given stage
def apriori(list_set,i):
    min_supp = 0.2        
   
    c = create_set(list_set,i)
    l = []
    for i in c:
        tmp = list(i)
        temp_supp = support(tmp)
        if temp_supp >= min_supp:
            l.append(tmp)
    return l
        
#Run program
def main():
    
    items  = count_unique_item(dataset)
    
    L = apriori(items,1)
    print("Frequent dataset of length 1 : ", apriori(items,1))
    print("Frequent set of length 2 : ", apriori(L,2))
   

main()

    




        
            

