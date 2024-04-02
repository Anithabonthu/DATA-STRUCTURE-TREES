#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Node: 
    def __init__(self,value): 
        self.left=None 
        self.data=value 
        self.right=None 
        
class BinarySearchTree: 
    def __init__(self): 
        self.root=None 
    def insert(self,value): 
        newnode=Node(value) 
        if self.root is None: 
            self.root=newnode 
        else: 
            current=self.root 
            while True: 
                if value<current.data: 
                    if current.left is None: 
                        current.left=newnode 
                        break 
                    else: 
                        current=current.left 
                elif current.data<value: 
                    if current.right is None: 
                        current.right=newnode 
                        break 
                    else: 
                        current=current.right 
                else: 
                    break 
    def search(self,d): 
        if self.root is None: 
            print("tree is Empty") 
        else: 
            current=self.root 
            while current:  
                if d==current.data:  
                    print("Element is Found")  
                    break  
                elif d<current.data:  
                    current=current.left  
                elif current.data<d:  
                    current=current.right  
            else:  
                print("Element Not found") 

    def inorder(self,current): 
        if current: 
            self.inorder(current.left) 
            print(current.data,end=" ") 
            self.inorder(current.right) 

             

bt=BinarySearchTree() 
while True: 
    print("1.insert  2.display   3.search  4.Exit") 
    ch=int(input("Enter your choice:")) 
    if ch==1: 
        value=int(input("Enter value:")) 
        bt.insert(value) 
    elif ch==2: 
        bt.inorder(bt.root)          
    elif ch==3: 
        key=int(input("enter element to search")) 
        bt.search(key) 
    elif ch==4: 
        break 

