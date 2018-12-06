
import numpy as np
import pandas as pd
import math
#%%
def get_partitions(column):
    partitions = {}
    entries = column
    #ent=0.0
    for entry in np.unique(entries):
        p = len(column[column==entry])/len(column)
        #ent -= p*math.log(p)/math.log(2)
        partitions[entry] = p
        
    return partitions

def get_entropy(data):
    target_y = data.iloc[:,-1]
    partitions_y = get_partitions(target_y)
    
    entropy = 0.0
    for p in partitions_y.items():
        p = list(p)
        entropy -= float((p[1])*math.log2(p[1]))
    return entropy

def get_gain(data,column):
    Es = get_entropy(data)
    gain = Es
    elements = data.loc[:,column]
    partitions_column = get_partitions(elements)
    
    for element in np.unique(elements):
        p = partitions_column[element]
        gain -= p*get_entropy(data.loc[data[column]==element,:])
    
    return gain

def decision_tree(data):
    d_tree = {}
    
    features = data.iloc[:,:-1].columns
    
    gains = {}
    
    for feature in features:
        gains[feature] = get_gain(data,feature)
    
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

original_data = pd.read_csv('data.csv')
original_data = original_data.drop("day",axis=1)

original_data.tail()

features = original_data.columns
dtree = decision_tree(original_data)


def draw(parent_name, child_name):
    edge = pydot.Edge(parent_name, child_name)
    graph.add_edge(edge)

def visit(node, parent=None):
    for k,v in node.items():
        if isinstance(v, dict):
            if parent:
                draw(parent, k)
            visit(v, k)
        else:
            draw(parent, k)
            draw(k, k+'_'+v)

import pydot

graph = pydot.Dot(graph_type='graph')
visit(dtree)
graph.write_png('example1_graph.png')
    


