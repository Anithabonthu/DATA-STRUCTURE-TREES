#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Node: 

    def __init__(self,v): 

        self.left=None 

        self.data=v 

        self.right=None 


class BinaryTree: 

    def __init__(self): 

        self.root=None 

    def create_root(self,value): 

        newnode = Node(value) 

        self.root=newnode 

        self.create_child(newnode) 

         

    def create_child(self,parent): 

        enq=input("is left child available for %d press y/n: "%parent.data).lower()

        if enq=='y': 

            lc=int(input("enter left child for %d: " %parent.data)) 

            parent.left=Node(lc) 

            self.create_child(parent.left) 

        enq=input("is right child available for %d:  press y/n: "%parent.data).lower()

        if enq=='y': 

            rc=int(input("enter right child for %d: " %parent.data)) 

            parent.right=Node(rc) 

            self.create_child(parent.right) 

    def preorder(self,current): 

        if current is None: 

            return  

        print(current.data) 

        self.preorder(current.left) 

        self.preorder(current.right) 

    def inorder(self,current): 

        if current is None: 

            return  

        self.inorder(current.left) 

        print(current.data) 

        self.inorder(current.right) 

    def postorder(self,current): 

        if current is None: 

            return  

        self.postorder(current.left) 

        self.postorder(current.right) 

        print(current.data) 

bt=BinaryTree() 

while True: 

    print("1.Create Tree 2.Preorder 3.|Inorder 4.Postorder 5.Exit") 

    ch=int(input("Enter choice: ")) 

    if ch==1: 

        rt = int(input("Enter root:")) 

        bt.create_root(rt) 

    elif ch==2: 

        bt.preorder(bt.root) 

    elif ch==3: 

        bt.inorder(bt.root) 

    elif ch==4: 

        bt.postorder(bt.root) 

    elif ch==5: 

        break 


# In[ ]:




