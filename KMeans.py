import numpy as np;
x1=[-2,-1];
x2=[-2,1];
x3=[-2,2];
x4=[-1,-1];
x5=[1,-1];
x6=[1,1];
x7=[1,2];
x8=[2,1];
x= [x1,x2,x3,x4,x5,x6,x7,x8];

prev_clusters = [[x1,x2,x3,x8],[x4],[x5,x6]];

def computeMean(clusters):
    return [np.sum(clusters[i],axis=0,dtype=np.float64)/len(clusters[i]) for i in range (len(clusters))];
    
    
def compute_distance(x,mean):
    return np.sum(np.square(x-mean));

new_clusters = [[],[],[]];


flag = False;

iteration =0;


while(flag==False):
    iteration = iteration+1;
    prev_means = computeMean(prev_clusters);
    new_clusters = [[],[],[]];
    for i in x:
        min_index = np.argmin([compute_distance(i,prev_means[0]),compute_distance(i,prev_means[1]),compute_distance(i,prev_means[2])]);
        new_clusters[min_index].append(i);
    
    flag = True
    for i in range(len(prev_clusters)):
        check = prev_clusters[i] == new_clusters[i];
        flag & check;
    
    prev_clusters = new_clusters;

print("Cluster 1",prev_clusters[0]);
print("Cluster 2",prev_clusters[1]);
print("Cluster 3",prev_clusters[2]);
