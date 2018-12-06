pt_in_cluster = 100 #int(input("Enter the points require in the cluster : "))
cluster_number = 2 #int(input("Enter the number of cluster require: "))
thres_dis = 25 #int(input("Enter the minimum threshold distance : "))


import random 
def generate_random_points(qty= pt_in_cluster, rangeX=100, rangeY=100):
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

def check_distance(x,y,list_of_pt):
    distance = abs((x-list_of_pt[0])+(list_of_pt[1]-y))
    return distance 



def make_cluster(n = pt_in_cluster,cluster_number = cluster_number):
    random_pt  = generate_random_points()
    center_pt = []
    clusters = []
    
    for i in range(cluster_number):
        temp = random.choice(random_pt)
        center_pt.append(temp)
        
        
    for i in range(cluster_number):
        temp = center_pt[i]
        temp_list = []
        for j,k in random_pt:
            if check_distance(j,k,temp)<=thres_dis:
                temp_list.append((j,k))
        clusters.append(temp_list)
    return clusters,center_pt

def difference(cluster):
    temp_list = []
    k,l = make_cluster()

    for i in range(len(cluster)):
        for m,n in l[i]:
            temp = check_distance(m,n,l[i])
            temp_list.append(temp)

    return temp_list