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
    
