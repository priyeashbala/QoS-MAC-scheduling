#!/usr/bin/env python
# coding: utf-8

# In[162]:


import math


# In[163]:


n = int(input('Enter the total number of Queues: '))
packets=[]

for i in range (0,n):
    print('Enter the number of packets in queue',i,'at time instant t: ')
    p = int(input())
    packets.append(p)



# <h3>Queues priority decreases from 0 to n-1</h3>
# 

# In[164]:


stat_weights=[]
for i in range (0,n):
    stat_weights.append(2) #Static weights for the queues are assumed to be 2. 
    
    


# <b> The static weights for the queues can be altered based on the priority and time sensitivity of the process. </b>

# In[165]:


total_packets=sum(packets)
total_packets_copy = total_packets
dyn_coeff=[]
dyn_weights=[]
dyn=[]
TX_complete=[]
h=0


# <h3> We are going to apply Dynamic Weighted Round Robin (D-WRR). </h3>

# In[166]:


while(total_packets_copy>0):
    h=h+1
    dyn_coeff=[]
    dyn_weights=[]    
    mean = total_packets_copy/n
    var=0
    for i in range (0,n):
        if(packets[i]>0):
            var = var + (packets[i]-mean)**2
    var = var/n
    rms = var**0.5
    for i in range (0,n):
        dyn_coeff.append(math.ceil(packets[i]/(rms+1)))
        dyn_weights.append(dyn_coeff[i]*stat_weights[i])        
    #print(dyn_weights)    
    dyn.append(dyn_weights)
    #print(dyn)
    while(sum(dyn_weights)>0):
        for i in range (0,n):
            if(dyn_weights[i]>0):
                if(packets[i]>0):
                    packets[i]=packets[i]-1
                    dyn_weights[i]=dyn_weights[i]-1
                    total_packets_copy=total_packets_copy-1
                else:
                    dyn_weights[i]=0
                    TX_complete.append([i,h])
            if(dyn_weights[i]==0 and packets[i]==0):
                TX_complete.append([i,h])
                packets[i]=-1

    packets
    
    


# In[167]:


TX=[]
TX.append(TX_complete[0])
for i in range (1,len(TX_complete)):
    p=0
    for j in range (0,len(TX)):
        if(TX_complete[i][0]==TX[j][0]):
            p=1
    if (p==0):
        TX.append(TX_complete[i])

    


# In[168]:


print("The number of cycles taken to complete the transmission of data in all",n,"queues is/are: ",len(dyn))
print("The cycle at which each of the ",n,"queues became empty is: ")
for i in range (0,n):
    print("Queue", i,"- ",TX[i][1]," cycle")

