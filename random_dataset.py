import random as rd
import numpy as np
list = ['apple','mango','pine','cheery','banana']
def random_dataset(list):
    item = []
    for i in range(len(list)-1):
        x  = rd.choice(list)
        item.append(x)
    return np.unique(item)


    