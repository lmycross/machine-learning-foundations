import numpy as np  
import pandas as pd  
import random

txt = np.loadtxt('data.txt')  
#txtDF = pd.DataFrame(txt)  
#txtDF.to_csv('data.csv',header=False,index=False)  

num=0
for s in range(0,2000):
    
    
    w=np.zeros((5,))

    txtran=txt.copy()
    
    np.random.seed()
    np.random.shuffle(txtran)
    x=txt[:,:-1]
    y=txt[:,-1]
    x0=np.ones((400,1))
    x=np.concatenate((x0,x),axis=1) 
    a,b=x.shape
    for i in range(a):
        
        h=x[i,:].dot(w)
        if h>0 and y[i]==-1:
            w+=-1*x[i,:]
            num+=1
        elif h<=0 and y[i]==1:
            w+=1*x[i,:]
            num+=1
    
    
print(num/2000)
#37
