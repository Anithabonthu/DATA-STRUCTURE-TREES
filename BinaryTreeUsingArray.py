#!/usr/bin/env python
# coding: utf-8

# In[ ]:


MAX_SIZE=20 

bt=[0]*MAX_SIZE 

print(bt) 

def create(i,value): 
 
    bt[i]=value 

    ch=input("is left child available for %d: Press y/n: "%value) 

    if ch=='y': 
        lc=int(input("Enter left child of %d: "%value)) 
        create(2*i+1,lc) 

    ch=input("is right child available for %d: Press y/n: "%value) 

    if ch=='y': 
        rc=int(input("Enter right child of %d: "%value)) 
        create(2*i+2,rc) 

def traverse(): 
    print(bt) 

def preorder(ind): 

    if ind>=MAX_SIZE or bt[ind]==0: 
        return  

    print(bt[ind]) 

    preorder(2*ind+1) 

    preorder(2*ind+2) 

  

def inorder(ind): 
    
    if ind>=MAX_SIZE or bt[ind]==0: 
        return  

    inorder(2*ind+1) 

    print(bt[ind]) 

    inorder(2*ind+2) 

   

def postorder(ind): 

    if ind>=MAX_SIZE or bt[ind]==0: 

        return  

    postorder(2*ind+1) 

    postorder(2*ind+2)   

    print(bt[ind]) 

while True: 

    print("1.create  2.Traversing 3.Preorder 4.Inorder 5.Postorder 6.exit") 

    ch=int(input("Enter choice:")) 

    if ch==1: 

        rt=int(input("enter root node")) 

        create(0,rt) 

    elif ch==2: 

        traverse() 

    elif ch==3: 

        preorder(0) 

    elif ch==4: 

        inorder(0) 

    elif ch==5: 

        postorder(0) 

    elif ch==6: 
        Break 


# In[ ]:





# In[ ]:




