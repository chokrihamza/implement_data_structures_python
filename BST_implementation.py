# queue for Level order traversal

class Queue(object):
    def __init__(self):
        self.items=[]
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
            
    def is_empty(self):
        return len(self.items)==0
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1].key
    # override len function
    def __len__(self):
        return len(self.items)








class BST:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None
    
    def insert(self,data):
        if self.key is None:
            self.key=data
            return 
        # ignore duplicate value 
        if self.key==data:
            return 
        if self.key > data:
            if self.lchild:
                  self.lchild.insert(data)
            else:
                  self.lchild=BST(data)
        
        else:
            if self.rchild:
                  self.rchild.insert(data)
            else:
                  self.rchild=BST(data)
        
     def search(self,data):
        if self.key==data:
            print("Node exist")
            return
        if self.key > data:
            if self.lchild:
                 self.lchild.search(data)
            else:
                print("Node is not present in te tree !!!")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not present in te tree !!!")
                
                
     def preorder(self):
     
        # root -> left -> right
        print(self.key)
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
            
            
            
            
    def inorder(self):
        """ left -> root -> right"""
        if self.lchild:
            self.lchild.inorder()
        print(self.key)
        if self.rchild:
            self.rchild.inorder()
            
            
            
            
    def postorder(self):
      
        if self.lchild :
           self.lchild.postorder() 
        if self.rchild:
           self.rchild.postorder()
        print(self.key)
        
        
        
    def delete(self,data):
        if self.key is None:
            print("Tree is empty !!!")
        if data<self.key:
            if self.lchild:
                self.lchild=self.lchild.delete(data)
            else:
                print("the node in not presented in the tree")
        elif data>self.key:
            if self.rchild:
                self.rchild=self.rchild.delete(data)
            else:
                print("the node in not presented in the tree")
        else:
            if self.lchild is None:
                temp=self.rchild
                self=None
                return temp
            if self.rchild is None:
                temp=self.lchild
                self=None
                return temp
            node=self.rchild
            while node.lchild:
                node=node.lchild
                
            self.key=node.key
            self.rchild=self.rchild.delete(node.key)
        return self
                
        
        
   def level_order_traversal(self,start):
        if start is None:
            return 
        queue=Queue()
        queue.enqueue(start)
        while queue:
            node=queue.dequeue()
            print(node.key)
            if node.lchild:
                queue.enqueue(node.lchild) 
            if node.rchild:
                queue.enqueue(node.rchild) 

root=BST(10)
#root.lchild=BST(5)
#print(root.key,root.lchild.lchild,root.rchild)
list1=[6,3,1,6,98,3,7]
for i in list1:
    root.insert(i)

#root.search(2)
print("preorder traversal")
root.preorder()
print("inorder traversal")
root.inorder()
print("postorder traversal")

root.delete(6)
root.delete(7)
root.delete(98)
root.postorder()
    

root=BST(10)
#root.lchild=BST(5)
#print(root.key,root.lchild.lchild,root.rchild)
list1=[6,3,1,6,98,3,7]
for i in list1:
    root.insert(i)

#root.search(2)
print("preorder traversal")
root.preorder()
print("inorder traversal")
root.inorder()
print("postorder traversal")
root.postorder()
        

root=BST(10)
root.lchild=BST(5)
print(root.key,root.lchild.lchild,root.rchild)
list1=[20,4,30,4,1,5,6]
for i in list1:
    root.insert(i)
    
