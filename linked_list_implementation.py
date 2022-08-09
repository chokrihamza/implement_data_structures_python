# implementation of linkedlist 

class Node:
    def __init__(self,data):
        """initilize our node"""
        self.data=data
        self.ref=None
class LinkedList:
    def __init__(self):
        """initilize our linked list"""
        self.head=None
    # traverse a linked list 
    def print_ll(self):
        """Print the linked list nodes"""
        if self.head is None:
            print("the linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
                
    def add_begin(self,data):
        """add node at the begeninng of the linked list"""
        # create a node 
        new_node=Node(data)
        # ref the new_node to the head of the linked list 
        new_node.ref=self.head
        self.head=new_node
    def add_end(self,data):
        """add node at the end of the linked list"""
        # create the new_node 
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node
    def add_after(self,data,x):
        n=self.head
        while n is not None:
            if n.data==x:
                break
            n=n.ref 
        if n is None:
            print("item not presented in the list")
        else:
             new_node = Node(data)
             new_node.ref = n.ref
             n.ref = new_node
    def add_before(self,data,x):
        if self.head is None:
            print("Linked list is empty")
            return 
        if self.head.data==x:
            new_node=Node(data)
            new_node.ref=self.head
            self.head=new_node 
            return 
        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n=n.ref
        if n.ref is None:
            print("Node is not found")
        else:
             new_node=Node(data)
             new_node.ref=n.ref
             n.ref=new_node
        
            
        
ll1=LinkedList()     
ll1.add_begin(10)
ll1.add_before(20,10)
ll1.add_after(50,10)
ll1.add_end(100)
ll1.add_begin(0)
ll1.print_ll()
    

    
        


        
