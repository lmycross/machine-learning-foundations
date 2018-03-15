import numpy as np  
import pandas as pd  
import random

train = np.loadtxt('train.txt')  
test = np.loadtxt('test.txt')  

#txtDF = pd.DataFrame(txt)  
#txtDF.to_csv('data.csv',header=False,index=False)  

x=train[:,:-1]
y=train[:,-1]
x0=np.ones((500,1))
x=np.concatenate((x0,x),axis=1) 
a,b=x.shape


xt=test[:,:-1]
yt=test[:,-1]
xt0=np.ones((500,1))
xt=np.concatenate((xt0,xt),axis=1) 
at,bt=xt.shape

num=0

def check(xran,w):
    right=0
    for i in range(a):
        h=xran[i,:].dot(w)
        if (h<=0 and y[i]==-1) or (h>0 and y[i]==1):
            right+=1
    return right


def te(xran,w):
    right=0
    for i in range(a):
        h=xran[i,:].dot(w)
        if (h<=0 and yt[i]==-1) or (h>0 and yt[i]==1):
            right+=1
    return right

for s in range(2000):
    
    
    w=np.zeros((5,))

    xran=x.copy()
    random.seed(s)
    random.shuffle(xran)
    iteration=[]
    for i in range(100):
        
        h=xran[i,:].dot(w)
        if h>0 and y[i]==-1:
            wnew=w-1*xran[i,:]
            if check(xran,wnew)>check(xran,w):
                w=wnew
        elif h<=0 and y[i]==1:
            wnew=w+1*xran[i,:]
            if check(xran,wnew)>check(xran,w):
                w=wnew
    num+=te(xt,w) 

print(num/2000/500)      
    
    
    



