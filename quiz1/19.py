import numpy as np  
import pandas as pd  
import random

train = np.loadtxt('train.txt')  
test = np.loadtxt('test.txt')  


xt=test[:,:-1]
yt=test[:,-1]
xt0=np.ones((500,1))
xt=np.concatenate((xt0,xt),axis=1) 
at,bt=xt.shape

num=0

def te(xran,w,yt):
    wrong=0
    for i in range(at):
        h=xran[i,:].dot(w)
        if (h<=0 and yt[i]==1) or (h>0 and yt[i]==-1):
            wrong+=1
    return wrong


num=0
for s in range(2000):
    
    
    w=np.zeros((5,))

    trainran=train.copy()
    random.seed()
    random.shuffle(trainran)
    x=trainran[:,:-1]
    y=trainran[:,-1]
    x0=np.ones((500,1))
    x=np.concatenate((x0,x),axis=1) 
    a,b=x.shape
    
    for i in range(50):
        
        h=x[i,:].dot(w)
        if h>0 and y[i]==-1:
            w+=-1*x[i,:]
            
        elif h<=0 and y[i]==1:
            w+=1*x[i,:]
            
    num+=te(xt,w,yt)
    
print(num/2000/500)
#0.310159

