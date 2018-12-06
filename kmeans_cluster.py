import random 
thres_dis = int(input("Enter the Minimum Threshold distance : "))

cluster_number  = int(input("Enter the Number of clustere required : "))

pt_in_cluster = int(input("Enter the Number of Points in a cluster : "))


def generate_random_points(qty, rangeX=100, rangeY=100):
    i = 0
    randpoints = []
    while i < qty:
        x = random.randrange(rangeX)
        y = random.randrange(rangeY)
        if (x,y) in randpoints: 
            continue
        randpoints.append((x,y))
        i += 1
    return randpoints

temp_pt = generate_random_points(pt_in_cluster)
Pt_list = []
for i in range(cluster_number):
        x = list(random.choice(temp_pt))    
        Pt_list.append(x)


import math
def check_distance(i,j,list_of_point):
    
    distance = math.sqrt((list_of_point[0]-i)*(list_of_point[0]-i)+(list_of_point[1]-j)*(list_of_point[1]-j))
    return distance

def cluster(n=pt_in_cluster,cluster_number=cluster_number,pt_list=Pt_list):
    temp_pt = generate_random_points(n)

    list_of_clusters = []     

    for i in range(cluster_number):
        cluster = []
        for k,l in temp_pt:
            if check_distance(k,l,pt_list[i])<=thres_dis:
                cluster.append((k,l))
        list_of_clusters.append(cluster)
    return list_of_clusters

intial_cluster = cluster(pt_in_cluster,cluster_number,Pt_list)

def mean(cluster,i):
    
    temp  = cluster[i]
    Xvalue = 0
    Yvalue = 0

    for k,l in temp:
        Xvalue = Xvalue + k
        Yvalue = Yvalue + l

    X = Xvalue/len(temp)
    Y = Yvalue/len(temp)
    return list((X,Y))

import matplotlib.pyplot as plt
import numpy as np

def main(n=pt_in_cluster,cluster_number=cluster_number,pt_list= Pt_list):

    dis = 1
    cluster_in = cluster()    
    while dis <=200:
        mean_cluster_pt = []
        for i in range(cluster_number):
            temp_pt = mean(cluster_in,i)
            mean_cluster_pt.append(temp_pt)    
        cluter_in = cluster(n,cluster_number,mean_cluster_pt)
        dis = dis + 2
    return cluster_in

def plot_cluster():
    temp = main()
    
    for i,j in temp[0]:
        x_plot = []
        y_plot = []

        x_plot.append(i)
        y_plot.append(j)
        plt.scatter(x_plot,y_plot,s= 15, c= 'red')
    for i,j in temp[1]:
        x_plot = []
        y_plot = []
        x_plot.append(i)
        y_plot.append(j)
        plt.scatter(x_plot,y_plot,s= 15, c= 'g')

    for i,j in temp[2]:
        x_plot = []
        y_plot = []

        x_plot.append(i)
        y_plot.append(j)
        plt.scatter(x_plot,y_plot,s= 15, c= 'blue')
    return plt.show()
