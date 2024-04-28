#!/usr/bin/env python
# coding: utf-8

# In[6]:


class Node: 
    def __init__(self,value): 
        self.left=None 
        self.data=value 
        self.right=None 


class BinarySearchTree: 
    def __init__(self): 
        self.root=None       
    def insert(self,rt,value):
        if not rt:
            return Node(value)
        elif value<rt.data:
            rt.left=self.insert(rt.left,value)
        elif value>rt.data:
            rt.right=self.insert(rt.right,value)
        return rt
         
    def inorder(self,current,l): 
        if current: 
            self.inorder(current.left,l) 
            l.append(current.data) 
            self.inorder(current.right,l) 
        return l


bt=BinarySearchTree() 
while True: 
    print("1.insert  2.Inorder  3.exit") 
    ch=int(input("Enter your choice:")) 
    if ch==1: 
        value=int(input("Enter value:")) 
        bt.root=bt.insert(bt.root,value) 
    elif ch==2:
        if not bt.root:
            print("Tree is empty")
        else:
            print(bt.inorder(bt.root,[]))          #it will display in increasing order 
    elif ch==3: 
        break 
k=int(input("Enter k value to print Kth Smallest value: "))
l1=bt.inorder(bt.root,[])
print(l1[k-1])



# In[ ]:




