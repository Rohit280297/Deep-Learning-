import numpy as np;


class DataPoints :
    def __init__(self,position,classIndex):
        self.position = position;
        self.classIndex = classIndex;
        self.distance = 0;


x1 = DataPoints([-2, -1],1);
x2 = DataPoints([-2, 1],2);
x3 = DataPoints([-2, 2],2);
x4 = DataPoints([-1, -1],1);
x5 = DataPoints([1, -1],1);
x6 = DataPoints([1, 1],3);
x7 = DataPoints([1, 2],3);
x8 = DataPoints([2, 1],3);

testData = DataPoints([-1,1],-1);

x = [x1,x2,x3,x4,x5,x6,x7,x8];

clusters = 3;

def compute_distance(x,testData):
    return np.sqrt(np.sum(np.square(x - testData)));


for i in x:
    i.distance = compute_distance(np.asarray(i.position),np.asarray(testData.position));

x.sort(key=lambda k:k.distance,reverse=False);

freq = [0]*clusters;

for i in range(clusters):
    freq[x[i].classIndex-1] = freq[x[i].classIndex-1] + 1;

print("Classified Class : ",np.argmax(freq)+1);