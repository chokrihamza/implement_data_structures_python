# implement a double linked list in python 
class Node:
    def __init__(self,data):
        self.data=data
        self.pref=None
        self.nref=None 
        
        
class DoubleLinkedList:
    def __init__(self):
        self.head=None
    def print_ll(self):
        """ Function to traverse double linked list forward"""
        if self.head==None:
            print("Linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.nref
    def print_ll_reverse(self):
        """ Function to traverse double linked list backward"""
        if self.head is None:
            print("Linked list is empty")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data)
                n=n.pref
            
    def insert_empty(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            priny("the linked list is not empty")
            
    def add_begin(self ,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.nref=self.head
            self.head.pref=new_node
            self.head=new_node
    
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node 
        else:
            # nove to the tail 
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.nref=new_node
            new_node.pref=n
    def add_after(self,data,x):
       
        if self.head==None:
            print("you can't insert : the double linked list is empty")
        else:
            n=self.head
            while n is not None:
                if n.data==x:
                   break
                n=n.nref
            if n is None:
                print("the node isn't in the linked list !!!")
            else:
                 new_node=Node(data)
                 new_node.nref=n.nref
                 new_node.pref=n
                 if n.nref is not None:
                     n.nref.pref=new_node 
                 n.nref=new_node
    def add_before(self,data,x):
        if self.head==None:
            print("you can't insert : the double linked list is empty")
        else:
            n=self.head
            while n is not None:
                if n.data==x:
                    break
                n=n.nref
            if n is None:
                print("the node isn't in the linked list !!!")
            else:
                new_node=Node(data)
                new_node.nref=n
                new_node.pref=n.pref
                if n.pref is not None:
                    n.pref.nref=new_node
                else:
                    self.head=new_node
                n.pref=new_node
                
     def delete_begin(self):
        if self.head is None:
            print("you can't delete the linked list is empty ")
            return
        if self.head.nref is None:
            self.head=None
            print("the linked list now is empty ")
        else:
            self.head=self.head.nref
            self.head.pref=None      
                 
    def delete_end(self):
        if self.head is None:
            print("you can't delete the linked list is empty ")
            return
        if self.head.nref is None:
            self.head=None
            print("the linked list now is empty ")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            
            n.pref.nref=None
              
            
     def delete_by_value(self,x):
        if self.head is None:
            # if the double linked list is empty 
            print("you can't delete the linked list is empty ")
            return
        if self.head.nref is None:
            # if the node is a head 
              if self.head.data==x:
                  self.head=None
              else:
                  print("x not equal the value in the node")
              return 
           
        if self.head.data==x:
            # if it's the first node 
            self.head=self.head.nref
            self.head.pref=None
            return 
        n=self.head
        while n.nref is not None :
            if n.data==x:
                break
            n=n.nref
        if n.nref is not None :
            n.pref.nref=n.nref
            n.nref.pref=n.pref
        else:
            if n.data==x:
                  n.pref.nref=None
            else:
                print("x is not exist in the double linked list")
            
        
        
            
        
        
        
        
        
        
        
        
        
            
        
            
            
            
doublell= DoubleLinkedList()
doublell.insert_empty(10)
doublell.add_begin(20)
doublell.add_after(30,20)
doublell.add_after(25,30)
doublell.add_before(5,10)
doublell.add_before(2,5)
doublell.add_end(50)
doublell.delete_begin()
doublell.delete_end()
doublell.delete_end()
doublell.delete_by_value(5)
print("------------------Begin--------------------------")
doublell.print_ll()
print("------------------Reverse------------------")
doublell.print_ll_reverse()       
