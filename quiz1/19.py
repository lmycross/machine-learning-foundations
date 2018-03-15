import numpy as np  
import pandas as pd  
import random

trainset = np.loadtxt('train.txt')  
testset = np.loadtxt('test.txt')  

xt=testset[:,:-1]
yt=testset[:,-1]
at,bt=xt.shape
xt0=np.ones((at,1))
xt=np.concatenate((xt0,xt),axis=1) 

num=0

def sign(input):
    if input<=0:
        return -1
    else:
        return 1
    
def check(inputs,w,y):
    error=0
    for i in range(a):
        h=inputs[i,:].dot(w)
        if sign(h) != y[i]  :
            error+=1
    return error


def test(inputs,w,yt):
    error=0
    for i in range(at):
        h=inputs[i,:].dot(w)
        if sign(h) != yt[i]:
            error+=1
    return error

for s in range(2000):
       
    x=trainset[:,:-1]
    a,b=x.shape
    y=trainset[:,-1]
    x0=np.ones((a,1))
    x=np.concatenate((x0,x),axis=1) 
    
    w=np.zeros((b+1,))
    w_best=np.zeros((b+1,))
    
    iterate = 0 
    iterateTimes=50
    while iterate <= iterateTimes:
        random.seed()
        dataIdx = random.randint(0, a-1)  
        
        h=x[dataIdx,:].dot(w)
        if sign(h) != y[dataIdx]:
            iterate += 1  
            w+=y[dataIdx]*x[dataIdx,:]

    num+=test(xt,w,yt) 

print(num/2000/at)      
#0.277897  
    
    







